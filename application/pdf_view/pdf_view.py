from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                              QLineEdit, QPushButton, QScrollArea, QWidget,
                              QFileDialog, QMessageBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import Table, TableStyle
import io
import os
import time
import math
from PIL import Image

class PdfPreviewDialog(QDialog):
    def __init__(self, order_data, user_data, parent=None):
        super().__init__(parent)
        self.order_data = order_data
        self.user_data = user_data
        self.additional_fields = {}
        
        self.setWindowTitle("Prévisualisation PDF")
        self.setMinimumSize(800, 600)

        self.width, self.height = A4
        self.margin = 20 * mm  # Marges de 20mm
        
        # Layout principal
        main_layout = QHBoxLayout()
        
        # Zone de gauche pour les champs
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        
        # Champs existants
        for key, value in order_data.items():
            field_layout = QHBoxLayout()
            label = QLabel(key.replace('_', ' ').title() + ":")
            value_label = QLabel(str(value))
            field_layout.addWidget(label)
            field_layout.addWidget(value_label)
            left_layout.addWidget(self.create_field_widget(label, value_label))
        
        # Champs additionnels
        self.compagny = self.add_additional_field("Compagny", left_layout)
        self.email = self.add_additional_field("Email", left_layout)
        self.adresse = self.add_additional_field("Adresse", left_layout)
        self.phone = self.add_additional_field("Téléphone", left_layout)
        self.notes = self.add_additional_field("Notes", left_layout)
        
        # Boutons
        buttons_layout = QHBoxLayout()
        preview_button = QPushButton("Actualiser l'aperçu")
        preview_button.clicked.connect(self.update_preview)
        download_button = QPushButton("Télécharger PDF")
        download_button.clicked.connect(self.download_pdf)
        
        buttons_layout.addWidget(preview_button)
        buttons_layout.addWidget(download_button)
        left_layout.addLayout(buttons_layout)
        
        left_layout.addStretch()
        
        # Zone de droite pour la prévisualisation
        preview_widget = QWidget()
        preview_layout = QVBoxLayout(preview_widget)
        preview_label = QLabel("Prévisualisation")
        self.preview_scroll = QScrollArea()
        self.preview_scroll.setWidgetResizable(True)
        self.preview_content = QLabel()
        self.preview_content.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.preview_scroll.setWidget(self.preview_content)
        
        preview_layout.addWidget(preview_label)
        preview_layout.addWidget(self.preview_scroll)
        
        # Ajout des zones au layout principal
        main_layout.addWidget(left_widget, 1)
        main_layout.addWidget(preview_widget, 2)
        
        self.setLayout(main_layout)
        
        # Générer la première prévisualisation
        self.update_preview()
    
    def create_field_widget(self, label, value_widget):
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.addWidget(label)
        layout.addWidget(value_widget)
        layout.addStretch()
        return widget
    
    def add_additional_field(self, field_name, layout):
        field_layout = QHBoxLayout()
        label = QLabel(field_name + ":")
        line_edit = QLineEdit()
        self.additional_fields[field_name] = line_edit
        field_layout.addWidget(label)
        field_layout.addWidget(line_edit)
        layout.addLayout(field_layout)
        return line_edit
    
    def generate_pdf(self, output_file=None):
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=A4)
        date = time.localtime()
        
        # Titre
        c.setFont("Helvetica-Bold", 24)
        c.setFillColor(colors.Color(0.7, 0.7, 0.8))  # Couleur bleu gris
        c.drawString(self.margin, self.height - self.margin - 10*mm, "BON DE COMMANDE")
        
        # Informations d'en-tête
        c.setFont("Helvetica", 10)
        c.setFillColor(colors.black)
        
        # Bloc société (en haut à gauche)
        y_pos = self.height - self.margin - 20*mm
        c.drawString(self.margin, y_pos, "Nom de la société : Gestionix")
        c.drawString(self.margin, y_pos - 5*mm, "Adresse : 10 rue Gilbert Dru")
        c.drawString(self.margin, y_pos - 10*mm, "Ville, code postal : Lyon, 69007")
        c.drawString(self.margin, y_pos - 15*mm, "Date : " + str(date.tm_mday) + "/" + str(date.tm_mon) + "/" + str(date.tm_year))
        
        # Blocs VENDEUR et ADRESSÉ À
        y_pos = self.height - self.margin - 50*mm
        
        # Bloc VENDEUR
        c.setFont("Helvetica-Bold", 10)
        c.drawString(self.margin, y_pos, "VENDEUR : Gestionix")
        c.setFont("Helvetica", 10)
        y_pos -= 10*mm
        fields = [
            ("Nom du contact : " + self.user_data.username), 
            ("Nom de la société cliente : Gestionix"), 
            ("Adresse : 10 Rue Gilbert Dru"), 
            ("Téléphone : 04.99.20.30.40")
        ]
        for field in fields:
            c.drawString(self.margin, y_pos, field)
            y_pos -= 8*mm
        
        # Bloc ADRESSÉ À
        y_pos = self.height - self.margin - 50*mm
        c.setFont("Helvetica-Bold", 10)
        c.drawString(self.width/2, y_pos, "ADRESSÉ À : " + self.order_data['customer'])
        c.setFont("Helvetica", 10)
        y_pos -= 10*mm
        fields = [
            ("Nom/Service : " + self.compagny.text()),
            ("Adresse : " + self.adresse.text()),
            ("Téléphone : " + self.phone.text()),
            ("E-mail : " + self.email.text())
        ]
        for field in fields:
            c.drawString(self.width/2, y_pos, field)
            y_pos -= 8*mm

        # Section Tableau

        price_str = self.order_data['total_price'].replace('€', '')
        price_int = float(price_str)
        y_pos = self.height - self.margin - 70*mm

        # Définir l'en-tête et les données en une seule ligne
        headers = ["Product", "Quantity", "Unity price", "Date of order"]
        data = [
            headers,
            [
                str(self.order_data['product']),
                str(self.order_data['quantity']), 
                str(price_int / int(self.order_data['quantity'])),
                str(self.order_data['date'])
            ]
        ]
        col_widths = [self.width*0.2, self.width*0.1, self.width*0.1, self.width*0.4]

        # Créer la table avec les données en ligne
        table = Table(data, colWidths=col_widths)

        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.Color(0.6, 0.6, 0.9)),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 8),
        ]))

        table.wrapOn(c, self.width, self.height)
        table.drawOn(c, self.margin, y_pos - 60*mm)
        # Section remarques
        y_pos = 120*mm
        c.drawString(self.margin, y_pos, "REMARQUES/NOTES")
        c.rect(self.margin, y_pos - 40*mm, self.width*0.5 - self.margin, 35*mm)
        
        # Section totaux
        y_pos = 120*mm
        total = float(price_int) * 1.2
        tva = total - float(price_int)

        totals = [
            ("SOUS-TOTAL", str(price_int)),
            ("TAUX TVA", "20,00%"),
            ("TOTAL TTC", str(math.ceil(tva)) + "€"),
            ("TOTAL", str(total))
        ]
        
        for i, (label, value) in enumerate(totals):
            c.drawRightString(self.width - self.margin - 50*mm, y_pos - i*8*mm, label)
            c.drawRightString(self.width - self.margin, y_pos - i*8*mm, value)
        
        # Signature
        c.drawRightString(self.width - self.margin - 50*mm, y_pos - 65*mm, "SIGNATURE")
        c.line(self.width - self.margin - 50*mm, y_pos - 70*mm, self.width - self.margin, y_pos - 70*mm)
        
        c.save()
        
        # Si un fichier de sortie est spécifié, sauvegarder le PDF
        if output_file:
            with open(output_file, 'wb') as f:
                f.write(buffer.getvalue())
        
        return buffer
    
    def update_preview(self):
        # Générer le PDF
        pdf_buffer = self.generate_pdf()
        
        try:
            from pdf2image import convert_from_bytes
            # Sur MacOS, spécifier explicitement le chemin de poppler
            poppler_path = '/opt/homebrew/bin'  # Chemin par défaut sur M1/M2
            # Pour Intel Mac, utilisez : '/usr/local/bin'
            
            images = convert_from_bytes(pdf_buffer.getvalue(), poppler_path=poppler_path)
            if images:
                preview_image = images[0]
                with io.BytesIO() as bio:
                    preview_image.save(bio, 'PNG')
                    pixmap = QPixmap()
                    pixmap.loadFromData(bio.getvalue())
                
                scaled_pixmap = pixmap.scaled(self.preview_scroll.size(), 
                                            Qt.AspectRatioMode.KeepAspectRatio,
                                            Qt.TransformationMode.SmoothTransformation)
                self.preview_content.setPixmap(scaled_pixmap)
        except Exception as e:
            # En cas d'erreur, afficher un message plus informatif
            error_message = (
                "Impossible de générer la prévisualisation.\n"
                "Assurez-vous que poppler est installé :\n"
                "brew install poppler\n\n"
                f"Erreur : {str(e)}"
            )
            self.preview_content.setText(error_message)
            self.preview_content.setWordWrap(True)
            
    def download_pdf(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Enregistrer le PDF",
            os.path.expanduser("~/Downloads/commande.pdf"),
            "PDF Files (*.pdf)"
        )
        
        if file_name:
            try:
                self.generate_pdf(file_name)
                QMessageBox.information(self, "Succès", "Le PDF a été enregistré avec succès!")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur lors de l'enregistrement du PDF: {str(e)}")
