import time
import sys
import subprocess
import requests
import wave
import os
install_results = subprocess.run(["pip3","install","pyaudio"], capture_output=True, text=True)
print(install_results.stdout)
import pyaudio
urls = ['https://i1.theportalwiki.net/img/3/34/GLaDOS_chellgladoswakeup01.wav', 'https://i1.theportalwiki.net/img/3/3d/GLaDOS_chellgladoswakeup04.wav', 'https://i1.theportalwiki.net/img/6/67/GLaDOS_chellgladoswakeup05.wav', 'https://i1.theportalwiki.net/img/3/30/GLaDOS_chellgladoswakeup06.wav', 'https://i1.theportalwiki.net/img/d/d6/GLaDOS_wakeup_outro01.wav', 'https://i1.theportalwiki.net/img/0/0c/GLaDOS_wakeup_outro02.wav']
player = pyaudio.PyAudio()
endcolor = ("\033[0m")
red = ("\033[31m")
redbri = ("\033[31;1m")
green = ("\033[32m")
greenbri = ("\033[32;1m")
VOICE = "Shelley"
time.sleep(2.0)
subprocess.run(["clear"])
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
while True:
        os.system("clear")
        print("")                                                             
        print("        GGGGGGGGGGGGG LLLLLLLLLLL                                DDDDDDDDDDDDD             OOOOOOOOO        SSSSSSSSSSSSSSS ")
        print("     GGG::::::::::::G L:::::::::L                                D::::::::::::DDD        OO:::::::::OO    SS:::::::::::::::S ")
        print("   GG:::::::::::::::G L:::::::::L                                D:::::::::::::::DD    OO:::::::::::::OO S:::::SSSSSS::::::S ")
        print("  G:::::GGGGGGGG::::G LL:::::::LL                                DDD:::::DDDDD:::::D  O:::::::OOO:::::::OS:::::S     SSSSSSS ")
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
        print("Genetic Lifeform and Disc Operating System")
        print("")
        print("")
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
                    os.system("clear")
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
                        time.sleep(0.5)
                        continue
                    elif postmodule == "2":
                        print("")
                        loading_screen("testing hydraulics... ")
                        print("HYDRAULICS READY")
                        print("")
                        time.sleep(0.5)
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
                                for url in urls:
                                    response = requests.get(url)
                                    with open('sound.wav', 'wb') as f:
                                        f.write(response.content)
                                    with wave.open('sound.wav', 'rb') as wave_file:
                                        stream = player.open(format=player.get_format_from_width(wave_file.getsampwidth()),
                                                             channels=wave_file.getnchannels(),  
                                                             rate=wave_file.getframerate(),
                                                             output=True)
                                        chunk_size = 1024
                                        data = wave_file.readframes(chunk_size)
                                        while data:
                                            stream.write(data)
                                            data = wave_file.readframes(chunk_size)
                                        stream.stop_stream()
                                        stream.close()
                                player.terminate()
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
            time.sleep(1.0)
            continue
        elif module == "3":
            print("")
            print(red,"ERROR: UNAVAILABLE",endcolor)
            print("")
            time.sleep(1.0)
            continue
        elif module == "4":
            print("")
            print(red,"ERROR: ALREADY RUNNING",endcolor)
            print("")
            time.sleep(1.0)
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
