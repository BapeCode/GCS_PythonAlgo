from colorama import Fore
class consoleManager:

    def send(self, message):
        print(f"[{Fore.MAGENTA + "GESTIONIX" + Fore.WHITE}] => {message}")

    def warn(self, message):
        self.send(Fore.YELLOW + message + Fore.WHITE)

    def success(self, message):
        self.send(Fore.GREEN + message + Fore.WHITE)

    def error(self, message):
        self.send(Fore.RED + message + Fore.WHITE)
    
    def debug(self, message):
        self.send(Fore.BLUE + message + Fore.WHITE)

console = consoleManager()