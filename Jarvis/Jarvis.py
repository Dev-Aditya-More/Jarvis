from colorama import Fore

from CmdInterpreter import CmdInterpreter

# from packages.memory.memory import Memory

"""
    AUTHORS' SCOPE:
        We thought that the source code of Jarvis would
        be more organized if we treat Jarvis as Object.
        So we decided to create this Jarvis Class which
        implements the core functionality of Jarvis in a
        simpler way than the original __main__.py.
    HOW TO EXTEND JARVIS:
        In progress..
    DETECTED ISSUES:
        * Furthermore, "near me" command is unable to find
        the actual location of our laptops.
"""


class Jarvis(CmdInterpreter):
    # We use this variable at Breakpoint #1.
    # We use this in order to allow Jarvis say "Hi", only at the first
    # interaction.
    first_reaction_text = ""
    first_reaction_text += Fore.BLUE + 'Jarvi\'s sound is by default disabled.' + Fore.RESET
    first_reaction_text += "\n"
    first_reaction_text += Fore.BLUE + 'In order to let Jarvis talk out loud type: '
    first_reaction_text += Fore.RESET + Fore.RED + 'enable sound' + Fore.RESET
    first_reaction_text += "\n"
    prompt = Fore.RED + "~> Hi, what can i do for you?\n" + Fore.RESET

    # This can be used to store user specific data

    def __init__(self, first_reaction_text=first_reaction_text,
                 prompt=prompt, first_reaction=True, enable_voice=False):
        """
        This constructor contains a dictionary with Jarvis Actions (what Jarvis can do).
        In alphabetically order.
        """
        CmdInterpreter.__init__(self, first_reaction_text, prompt, first_reaction, enable_voice)

        self.actions = ("ask",
                        "chat",
                        {"check": ("ram",)},
                        "chuck",
                        {"decrease": ("volume",)},
                        "directions",
                        {"disable": ("sound",)},
                        {"enable": ("sound",)},
                        "error",
                        "evaluate",
                        "exit",
                        "goodbye",
                        "help",
                        {"hotspot": ("start", "stop")},
                        {"increase": ("volume",)},
                        "match",
                        "movies",
                        "music",
                        "near",
                        "news",
                        {"open": ("camera",)},
                        "pinpoint",
                        "os",
                        "quit",
                        "remind",
                        "say",
                        {"screen": ("off",)},
                        {"display": ("pics",)},
                        "shutdown",
                        "reboot",
                        "todo",
                        {"update": ("location", "system")},
                        "weather",
                        )

        self.fixed_responses = {"what time is it": "clock",
                                "where am i": "pinpoint",
                                "how are you": "how_are_you"
                                }

    def speak(self):
        if self.enable_voice:
            self.speech.speak(self.first_reaction)

    def find_action(self, data):
        """This method gets the data and assigns it to an action"""
        output = "None"

        data = data.lower()
        data = data.replace("?", "")
        data = data.replace(",", "")

        # Check if Jarvis has a fixed response to data
        if data in self.fixed_responses:
            output = self.fixed_responses[data]  # change return to output =
        else:
            # if it doesn't have a fixed response, look if the data corresponds to an action
            words = data.split()
            words_aux = data.split()

            action_found = False
            for word in words:
                words_aux.remove(word)
                for action in self.actions:
                    if type(action) is dict and word in action.keys():
                        action_found = True
                        output = word
                        if len(words_aux) != 0:
                            words_aux_aux = list(words_aux)
                            for word_aux in words_aux:
                                words_aux_aux.remove(word_aux)
                                for value in action[word]:
                                    if word_aux == value:
                                        output += " " + word_aux
                                        output += " " + " ".join(words_aux_aux)
                        break
                    elif word == action:
                        action_found = True
                        output = word
                        break
                if action_found:
                    break

        return output

    def executor(self):
        """
        This method is opening a terminal session with the user.
        We can say that it is the core function of this whole class
        and it joins all the function above to work together like a
        clockwork. (Terminates when the user send the "exit", "quit"
        or "goodbye command")
        :return: Nothing to return.
        """
        self.speak()
        self.cmdloop(self.first_reaction_text)

