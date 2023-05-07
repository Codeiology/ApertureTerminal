import time
import sys
import subprocess
import threading
endcolor = ("\033[0m")
red = ("\033[31m")
redbri = ("\033[31;1m")
green = ("\033[32m")
greenbri = ("\033[32;1m")
VOICE = "Shelley"
time.sleep(2.0)
def loading_screen(message):
    print(message, end="")
    spinner = ["|", "/", "-", "\\"]
    start_time = time.time()
    i = 0
    while True:
        if time.time() - start_time > 3:
            print("\b \b" * (len(message) + 1), end="")
            break
        print(f"\b{spinner[i%4]}", end="", flush=True)
        i += 1
        time.sleep(0.05)
        
def type_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()
print("")                                                             
print("        GGGGGGGGGGGGG LLLLLLLLLLL                                DDDDDDDDDDDDD             OOOOOOOOO        SSSSSSSSSSSSSSS ")
print("     GGG::::::::::::G L:::::::::L                                D::::::::::::DDD        OO:::::::::OO    SS:::::::::::::::S ")
print("   GG:::::::::::::::G L:::::::::L                                D:::::::::::::::DD    OO:::::::::::::OO S:::::SSSSSS::::::S ")
print(" G:::::GGGGGGGG::::G LL:::::::LL                                DDD:::::DDDDD:::::D  O:::::::OOO:::::::OS:::::S     SSSSSSS ")
print(" G:::::G       GGGGGG   L:::::L                  aaaaaaaaaaaaa      D:::::D    D:::::D O::::::O   O::::::OS:::::S ")
print("G:::::G                 L:::::L                  a::::::::::::a     D:::::D     D:::::DO:::::O     O:::::OS:::::S ")
print("G:::::G                 L:::::L                  aaaaaaaaa:::::a    D:::::D     D:::::DO:::::O     O:::::O S::::SSSS ")
print("G:::::G    GGGGGGGGGG   L:::::L                           a::::a    D:::::D     D:::::DO:::::O     O:::::O  SS::::::SSSSS ")
print("G:::::G    G::::::::G   L:::::L                    aaaaaaa:::::a    D:::::D     D:::::DO:::::O     O:::::O    SSS::::::::SS ")  
print("G:::::G    GGGGG::::G   L:::::L                  aa::::::::::::a    D:::::D     D:::::DO:::::O     O:::::O       SSSSSS::::S ")
print("G:::::G        G::::G   L:::::L                 a::::aaaa::::::a    D:::::D     D:::::DO:::::O     O:::::O            S:::::S ")
print(" G:::::G       G::::G   L:::::L         LLLLLL a::::a    a:::::a    D:::::D    D:::::D O::::::O   O::::::O            S:::::S ")
print("  G:::::GGGGGGGG::::G LL:::::::LLLLLLLLL:::::L a::::a    a:::::a  DDD:::::DDDDD:::::D  O:::::::OOO:::::::OSSSSSSS     S:::::S ")
print("   GG:::::::::::::::G L::::::::::::::::::::::L a:::::aaaa::::::a  D:::::::::::::::DD    OO:::::::::::::OO S::::::SSSSSS:::::S ")
print("     GGG::::::GGG:::G L::::::::::::::::::::::L  a::::::::::aa:::a D::::::::::::DDD        OO:::::::::OO   S:::::::::::::::SS ")
print("        GGGGGG   GGGG LLLLLLLLLLLLLLLLLLLLLLLL   aaaaaaaaaa  aaaa DDDDDDDDDDDDD             OOOOOOOOO      SSSSSSSSSSSSSSS ")
print("")
print("")
while True:
    time.sleep(2.0)
    print("Currently loaded modules:")
    print("")
    time.sleep(0.1)
    print(" 1. Initialize GLaDOS ",redbri,"not running",endcolor)
    time.sleep(0.1)
    print(" 2. Test hydraulics ",redbri,"not running",endcolor)
    time.sleep(0.1)
    print(" 3. Boot GLaDOS ",red,"unavailable",endcolor)
    time.sleep(0.1)
    print(" 4. Initialize GLaDOS in passive REACT mode",green,"running",endcolor)
    time.sleep(0.1)
    print(" 5. Exit program")
    time.sleep(0.1)
    print(" 6. Shut down GLaDOS")
    time.sleep(0.1)
    print("")
    module = input("Choose one module: ")
    if module == "1":
        print("")
        code = input("Please insert initialization code provided by project overseer: ")
        print("")
        if code == "JAT4736251":
            print("accepted!")
            print("")
            loading_screen("quitting REACT mode... ")
            loading_screen("readying personnel and systems... ")
            loading_screen("Initializing GLaDOS... ")
            print("")
            print(green,"Success! Booting is now available.",endcolor)
            print("")
            time.sleep(2.0)
            print("Currently loaded modules:")
            print("")
            time.sleep(0.1)
            print(" 1. Initialize GLaDOS ",green,"running",endcolor)
            time.sleep(0.1)
            print(" 2. Test hydraulics ",redbri,"not running",endcolor)
            time.sleep(0.1)
            print(" 3. Boot GLaDOS ",greenbri,"ready",endcolor)
            time.sleep(0.1)
            print(" 4. Initialize GLaDOS in passive REACT mode",redbri,"not running",endcolor)
            time.sleep(0.1)
            print(" 5. Exit program")
            time.sleep(0.1)
            print(" 6. Shut down GLaDOS")
            time.sleep(0.1)
            print("")
            postmodule = input("Choose one module: ")
            if postmodule == "1":
                print("")
                print("ERROR: ALREADY RUNNING")
                continue
            elif postmodule == "2":
                print("")
                loading_screen("testing hydraulics... ")
                print("HYDRAULICS READY")
                print("")
                continue
            elif postmodule == "3":
                print("")
                code = input("Please insert initialization code provided by project overseer: ")
                print("")
                if code == "JAT4736251":
                    print("Please insure all personnell are ready for booting. GLaDOS is experimental AI and could lead to injury or death")
                    consent = input("are you sure you are ready to boot? (y/n): ")
                    if consent == "y":
                        print("")
                        loading_screen("readying systems... ")
                        loading_screen("Booting emotional dampening cores... ")
                        loading_screen("preparing... ")
                        loading_screen("Booting (please keep safe distance)... ")
                        print("")
                        subprocess.run(["clear"])
                        time.sleep(1.0)
                        subprocess.run(["say", "-v","Daniel", "powerup", "complete"])
                        time.sleep(1.5)
                        subprocess.run(["say", "-v", VOICE, "oh.", "It's", "you."])
                        type_text("Oh. Its you.")
                        time.sleep(1.0)
                        print("")
                        subprocess.run(["say", "-v", VOICE,"Its", "been", "a", "laung", "time"])
                        type_text("Its been a long time.")
                        time.sleep(0.2)
                        subprocess.run(["say", "-v", VOICE, "How", "have", "you", "been"])
                        print("")
                        type_text("How have you been?")
                        time.sleep(0.5)
                        subprocess.run(["say", "-v", VOICE, "I've", "been", "really", "busy", "being", "dead."])
                        print("")
                        type_text("I've been really busy being dead.")
                        print("")
                        time.sleep(1.0)
                        subprocess.run(["clear"])
                        subprocess.run(["say", "-v", "Grandma", "you", "know,", "after", "you", "killed", "me"])
                        type_text("you know. After you killed me.")
                        subprocess.run(["clear"])
                        subprocess.run(["say", "-v", "Cellos", "dum", "dum", "dee", "dum", "dum", "dum", "dum", "dee", "dum", "dum", "dee", "dum", "dum", "dum", "dum", "dee", "dum", "dee", "dum", "dum", "dum", "de", "dum", "dum", "dum", "dee"])
                        sys.exit()
        else:
            print("INCCORECT CODE. ABORTING")
            print("")
            continue
    elif module == "2":
        print("")
        print("")
        loading_screen("testing hydraulics... ")
        print("HYDRAULICS READY")
        print("")
        continue
    elif module == "3":
        print("")
        print(red,"ERROR: UNAVAILABLE",endcolor)
        print("")
        continue
    elif module == "4":
        print("")
        print(red,"ERROR: ALREADY RUNNING",endcolor)
        print("")
        continue
    elif module == "5":
        print("")
        loading_screen("Exiting... ")
        sys.exit()
    elif module == "6":
        print("")
        clearance = input("Enter a valid clearance code level 5: ")
        if clearance == "JAT4736251":
            loading_screen("shutting down GLaDOS... ")
            print("WARNING: SERVICE DOWN")
            sys.exit()
        else:
            print("")
            print("INVALID")
            continue
    else:
        print("")
        print("INVALID")
        continue