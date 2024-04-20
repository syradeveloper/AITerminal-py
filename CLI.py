import cmd
import asyncio
import traceback
import sys
import os
from io import StringIO
from libraries.pseudohacker import PseudoHacker
from libraries.ai import ArtificialInteligence

class AiTerminalCLI(cmd.Cmd):
    intro = """┌──────────────────┬────────────────────────────────────────────────────────────┐
│    AiTerminal                                                                 │
├──────────────────┴────────────────────────────────────────────────────────────┤
│                                                                               │
│                                                                               │
│              ░▒▓███████▓▒░░▒▓████████▓▒░▒▓████████▓▒░  ░▒▓█▓▒░                │
│                     ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓████▓▒░                │
│                     ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░                │
│               ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░                │
│              ░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░                │
│              ░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░                │
│              ░▒▓████████▓▒░▒▓███████▓▒░░▒▓████████▓▒░  ░▒▓█▓▒░                │
│                                                                               │
│                                                                               │
│  [•]   Welcome to the AiTerminal script!                                      │
│  [!]   Type "help" for more information...                                    │
│  [@]   You confirm that you have read and accept the MIT LICENSE.             │
│                                                                               │
└───────────────────────────────────────────────────────────────────────────────┘\n"""
    prompt = "[2501] > "

    def do_osint(self, text):
        """[phone number] :: Checks a phone number""" 
        try:
            PseudoHacker.checkphone(text)
        except Exception as e:
            print(f"Error: {str(e)}\n")

    def do_echo(self, text):
        """[text] :: Prints text to the console"""
        print(text)

    def do_cat(self, filename):
        """[filename] :: Displays the contents of a file"""
        try:
            with open(filename, "r") as file:
                content = file.read()
            print(content + "\n")
        except Exception as e:
            print(f"Error: {str(e)}\n")

    def do_mkdir(self, dirname):
        """[dirname] :: Creates a new directory"""
        try:
            os.mkdir(dirname)
        except Exception as e:
            print(f"Error: {str(e)}")

    def do_rmdir(self, dirname):
        """[dirname] :: Removes an empty directory"""
        try:
            os.rmdir(dirname)
        except Exception as e:
            print(f"Error: {str(e)}")

    def do_rm(self, filename):
        """[filename] :: Removes a file"""
        try:
            os.remove(filename)
        except Exception as e:
            print(f"Error: {str(e)}")

    def do_touch(self, filename):
        """[filename] :: Creates a new file"""
        try:
            with open(filename, "w") as file:
                pass
        except Exception as e:
            print(f"Error: {str(e)}")

    def do_ls(self, path):
        """[dirname] :: Lists files and directories in the current directory"""
        try:
            if not path:
                cpath = os.getcwd()
                files = os.listdir(cpath)
                print("\n".join(files) + "\n")
            else:
                cpath = path
                files = os.listdir(cpath)
                print("\n".join(files) + "\n")
        except Exception as e:
            print(path)
            print(f"Error: {str(e)}\n")
        
    def do_cd(self, path):
        """[dirname] :: Changes the current directory"""
        try:
            if not path:
                print(os.getcwd())
            elif path == "..":
                os.chdir(os.path.dirname(os.getcwd()))
                print(os.getcwd())
            else:
                os.chdir(path)
                print(os.getcwd())
        except Exception as e:
            print(f"Error: {str(e)}")

    def do_python(self, code):
        """[code] or [-c filename.py] | Executes Python code/Compile Python files"""
        try:
            if code.startswith("-c "):
                script_path = code[3:]
                with open(script_path, "r") as script_file:
                    script_content = script_file.read()
                stdout_backup = sys.stdout
                sys.stdout = StringIO()
                exec(script_content)
                result = sys.stdout.getvalue()
                print(result)
            else:
                stdout_backup = sys.stdout
                sys.stdout = StringIO()
                exec(code)
                result = sys.stdout.getvalue()
                print(result)
        except Exception as e:
            print(traceback.format_exc())
        finally:
            sys.stdout = stdout_backup

    def do_clear(self, args):
        """Clears the console"""
        os.system('cls' if os.name=='nt' else 'clear')
        print(self.intro)

    def do_exit(self, args):
        """Exits the console application"""
        return True

    def do_help(self, args):
        """Displays available commands and their descriptions"""
        for command in self.get_names():
            if command.startswith("do_"):
                command_name = command[3:]
                print(f"    {command_name} {getattr(self, command).__doc__}")


    def do_ai(self, command):
        """[Text] :: Allows the user to send an AI request | Expect delays with response"""
        asyncio.run(self.process_text(command))

    async def process_text(self, text):
        model = ArtificialInteligence()
        response = await model.generate_response(text)
        print("    " + response)

if __name__ == "__main__":
    AiTerminalCLI().cmdloop()
