import speech_recognition as sr
import os
import pyttsx3 as px

engine = px.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',130)
r = sr.Recognizer()
r.energy_threshold=5000

TGREEN = '\033[32m'
TWHITE = '\033[37m'
TYELLOW = '\033[33m'
TBLUE = '\033[34m'
TRED = '\033[31m'
TCYAN = '\033[36m'


print(TGREEN, '\t \t Welcome to the command assistant ')
px.speak("Welcome to the command assistant")

status = 1


def aboutSystem():
    print(TGREEN, '\t \t Welcome to the System Info ')

    while (True):
        px.speak("now your are having system info menu")
        if status == 1:
            print(TGREEN, ''' \t List of option to get information about the System :-
                       - Show the date : {} press 1 {}
                       - show the calender of this month : {} press 2 {}
                       - Show the calender of some specific month/year : {} press 3 {}
                       - Show the IP configurations : {} press 4 {}
                       - Show the Commands help : {} press 5 {}
                       - Show the list of files : {} press 6 {}
                       - Show the firewall status : {} press 7 {}
                       - Show availabe/unavailable softwares : {} press 8 {}
                       - Show the java version : {} press 9 {}
                       - Show the actual software name : {} press 10 {}
                       - Show the CPU information : {} press 11 {}
                       - Exit the program : {} press 0
            '''.format(TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW))
            
            #with sr.Microphone() as source:
                 #print("i am listening.....")
                 #m1audio = r.listen(source)
                 #px.speak("ok")
                 #print("please wait...")
                 #m1= r.recognize_google(m1audio)
                 #print(m1)
            m1 = input()

            if (('close' in m1) or ('exit' in m1) or ('quit' in m1)):
                print(TYELLOW, 'Exiting the program .....')
                break
            else:
                if (('show' in m1) or ('open' in m1) or ('run' in m1) or ('execute' in m1) or ('start' in m1)) and ('date' in m1):
                    print(TYELLOW, 'Showing the date.....', TWHITE)
                    os.system('date')

                elif (('show' in m1) or ('open' in m1) or ('run' in m1) or ('execute' in m1) or ('start' in m1)) and (('calendar' in m1) and ('this' in m1)):
                    print(TYELLOW, 'showing the calender of this month .....', TWHITE)
                    os.system('cal')

                elif (('show' in m1) or ('open' in m1) or ('run' in m1) or ('execute' in m1) or ('start' in m1)) and (('calendar' in m1) and ('specific' in m1)):
                    print(
                        TYELLOW, 'Showing the calender of some specific month/year .....', TWHITE)
                    month = int(input('enter the month : '))
                    year = int(input('enter the year : '))
                    os.system('cal {} {} '.format(month, year))

                elif (('show' in m1) or ('open' in m1) or ('run' in m1) or ('execute' in m1) or ('start' in m1)) and (('ip' in m1)):
                    print(TYELLOW, 'Showing the IP configurations .....', TWHITE)
                    os.system('ifconfig')

                elif (('show' in m1) or ('open' in m1) or ('run' in m1) or ('execute' in m1) or ('start' in m1)) and (('commands' in m1) and ('help' in m1)):
                    print(TYELLOW, 'Showing the commands  help  .....', TWHITE)
                    os.system('help')

                elif (('show' in m1) or ('open' in m1) or ('run' in m1) or ('execute' in m1) or ('start' in m1)) and (('list' in m1) and ('files' in m1)):
                    print(TYELLOW, 'Showing the list of files .....', TWHITE)
                    os.system('ls ')

                elif (('show' in m1) or ('open' in m1) or ('run' in m1) or ('execute' in m1) or ('start' in m1)) and (('firewall' in m1) and ('status' in m1)):
                    print(TYELLOW, 'Showing the firewall status .....', TWHITE)
                    os.system('systemctl status firewalld ')

                elif (('show' in m1) or ('open' in m1) or ('run' in m1) or ('execute' in m1) or ('start' in m1)) and (('available' in m1) and ('softwares' in m1)):
                    print(TYELLOW, 'Showing availabe/unavailable softwares .....', TWHITE)
                    softname = input('enter the name of software to check its availability : ')
                    os.system('rpm -q {}'.format(softname))

                elif (('show' in m1) or ('open' in m1) or ('run' in m1) or ('execute' in m1) or ('start' in m1)) and (('java' in m1) and ('version' in m1)):
                    print(TYELLOW, 'Showing the java version .....', TWHITE)
                    os.system('java -version')

                elif (('show' in m1) or ('open' in m1) or ('run' in m1) or ('execute' in m1) or ('start' in m1)) and (('software' in m1) and ('name' in m1)):
                    print(TYELLOW, 'Showing the actual software name .....', TWHITE)
                    softname = input(
                        'enter the value to fetch actual software name : ')
                    os.system('which  {} '.format(softname))

                elif (('show' in m1) or ('open' in m1) or ('run' in m1) or ('execute' in m1) or ('start'in m1)) and (('cpu' in m1) and ('information' in m1)):
                    print(TYELLOW, 'Showing the CPU information .....', TWHITE)
                    os.system('lscpu ')

                else:
                    px.speak("sorry try again")
                    print(TYELLOW, 'Choose a valid option !!!', TWHITE)
                    continue

            print(TBLUE, '\n ')
            cont = input(
                'Do you wants to continue with the System informatons ?[y/n] : ')
            if (cont == 'y') or (cont == 'Y'):
                continue
            else:
                break


def manageMultipleProgram():
    px.espeak("Welcome to Multi Task Manager")
    while (True):
        print(TGREEN, '\t \t Welcome to Multi Task Manager \n \n  ', TWHITE)
        px.speak("now you are in multitask manager menu")
        pgname = input('Enter the program name to be executed :  ')
        os.system('{} & '.format(pgname))

        print(TBLUE, '\n')
        cont = input('Do you wants to execute more programs ?[y/n] : ')
        if (cont == 'y') or (cont == 'Y'):
            continue
        else:
            break


def cacheManager():
    px.speak("Welcome to the cache Manager")
    while (True):
        print(TGREEN, '\t \t Welcome to the cache Manager \n  ')
        px.speak("now you are in the cache manager menu")
        print('''  \t List of operations that can be performed on the Cache memory :-
                    - Show the cache status : {} press 1 {}
                    - Remove the cache memory : {} press 2 {}
                    - Exit the cache manager : {} press 0
        '''.format(TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW))
        #with sr.Microphone() as source:
                 #print("i am listening.....")
                 #m1audio = r.listen(source)
                 #px.speak("ok")
                 #print("please wait...")
                 #m1 = r.recognize_google(m1audio)
                 #print(m1)
        m1=input()

        if (('exit' in m1) or ('quit'  in m1) or ('close' in m1)):
            print(TYELLOW, 'Exiting the program ..... ')
            break
        else:
            if (('show' in m1) or ('open' in m1) or ('run' in m1) or ('execute' in m1) or ('start' in m1)) and (('cache' in m1) and ('status' in m1)):
                print(TYELLOW, 'Showing the cache memory status ..... ', TWHITE)
                os.system('free -m ')

            elif (('show' in m1) or ('open' in m1) or ('run'  in m1) or ('execute' in m1) or ('start' in m1) or ('remove' in m1))and (('cache' in m1)):
                print(TYELLOW, 'Removing cache memory ..... ', TWHITE)
                os.system('echo  3 > /proc/sys/vm/drop_caches')

            else:
                px.speak("say it clearly")
                print(TYELLOW, 'Choose a valid option !!!', TWHITE)
                continue

        print(TBLUE, '\n ')
        cont = input('Do you wants to continue with the System informatons ?[y/n] : ')
        if (cont == 'y') or (cont == 'Y'):
            continue
        else:
            break


def binaryCalulator():
    px.speak("welcome to binary calculator")
    print(TYELLOW, 'Once the mathematical calculation is done, enter "quit" to come out of it !!', TWHITE)
    while (True):
        os.system('bc')
        print(TGREEN, '\n \n ')
        cont = input('Do you wants to use Binary Calculator again ?[y/n] : ')
        if (cont == 'y') or (cont == 'Y'):
            continue
        else:
            break


def fileManager():
    px.speak("Welcome to the file Manager")
    while (True):
        print(TGREEN, '\t \t Welcome to the file Manager \n  ')
        px.speak("now you are in file manager menu. tell me how can i help you with it")
        print('''  \t List of operations that can be performed with file Manager  :-
                    - Show a file's content : {} press 1 {}
                    - Create a new file : {} press 2 {}
                    - Exit the cache manager : {} press 0
        '''.format(TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW))
        #with sr.Microphone() as source:
                 #print("i am listening.....")
                 #m1audio = r.listen(source)
                 #px.speak("sure")
                 #print("sure...")
                 #m = r.recognize_google(m1audio)
                 #print(m)
        m = input()
        if ('exit' in m) or ('quit' in m) or ('close' in m):
            print(TYELLOW, 'Exiting the program ..... ')
            break
        else:
            if (('show' in m) or ('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) and (('file' in m) and ('content' in m)):
                print(TYELLOW, 'Showing the File Conetent ..... ', TWHITE)
                fileName = input(
                    'Enter the file name (with extension like abc.py, ab.txt ) : ')
                os.system('cat {}'.format(fileName))

            elif (('show' in m) or ('open' in m) or ('run' in m) or ('execute'in m) or ('start' in m)) and (('create' in m) and ('file' in m)):
                print(TYELLOW, 'Opening file editor ..... ', TWHITE)
                fileName = input(
                    'Enter the file name (with extension like abc.py, ab.txt ) : ')
                print(
                    TYELLOW, 'After writing your data to the file, Press Esc key then type :wq  then press Enter !!', TWHITE)
                os.system('vi  {}'.format(fileName))

            else:
                px.speak("say it clearly")
                print(TYELLOW, 'Choose a valid option !!!', TWHITE)
                continue

        print(TBLUE, '\n ')
        cont = input(
            'Do you wants to continue with the File Manager ?[y/n] : ')
        if (cont == 'y') or (cont == 'Y'):
            continue
        else:
            break


def connectionChecker():
    px.speak("welcome to connection checker")
    print(TGREEN, '\t \t Welcome to connection checker ', TWHITE)
    while(True):
        ip = input('Enter the IP where you wants to check the connection : ')
        os.system('ping -c 3 {}'.format(ip))
        print(TBLUE, '\n ')
        cont = input(
            'Do you wants to continue with the connection checker ?[y/n] : ')
        if (cont == 'y') or (cont == 'Y'):
            continue
        else:
            break


def processManager():
    px.speak("Welcome to the Process Manager")
    while (True):
        px.speak("now you are in process manager")
        print(TGREEN, '\t \t Welcome to the Process Manager \n  ')
        print('''  \t List of operations that can be performed with Process Manager :-
                    - Show the Stopped background processes : {} press 1 {}
                    - Show the running processes : {} press 2 {}
                    - Kill any running process : {} press 3 {}
                    - Exit the cache manager : {} press 0
        '''.format(TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW))
        #with sr.Microphone() as source:
                 #print("i am listening.....")
                 #m1audio = r.listen(source)
                 #px.speak("sure")
                 #print("sure...")
                 #m = r.recognize_google(m1audio)
                 #print(m)
        m=input()
        if ('exit' in m) or ('quit' in m) or ('close' in m):
            print(TYELLOW, 'Exiting the program ..... ')
            break
        else:
            if (('show' in m) or ('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) and (('stopped' in m) and ('background' in m)):
                print(
                    TYELLOW, 'Showing the Stopped background processes  ..... ', TWHITE)
                os.system('jobs ')

            elif (('show' in m) or ('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) and (('running' in m) and ('processes' in m)):
                print(TYELLOW, 'Showing the running processes ..... ', TWHITE)
                os.system('ps -aux ')

            elif (('show'in m )or ('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) and (('kill' in m) and ('running' in m)):
                print(TYELLOW, 'Kill any running process ..... ')
                print('Showing list of running processes :- ', TWHITE)
                os.system('ps -aux ')
                id = int(
                    input('Enter the ID of the process that you wants to kill : '))
                os.system('kill {}'.format(id))
                print(TYELLOW, 'Killed the process with PID {} '.format(id), TWHITE)

            else:
                px.speak("say it clearly")
                print(TYELLOW, 'Choose a valid option !!!', TWHITE)
                continue

        print(TBLUE, '\n ')
        cont = input(
            'Do you wants to continue with the Process Manager ?[y/n] : ')
        if (cont == 'y') or (cont == 'Y'):
            continue
        else:
            break


def userManager():
    px.speak("Welcome to the User Manager")
    while (True):
        print(TGREEN, '\t \t Welcome to the User Manager \n  ')
        px.speak("currently you are in user manager menu")
        print('''  \t List of operations that can be performed with User Manager :-
                    - Show the available users : {} press 1 {}
                    - Add a new user : {} press 2 {}
                    - Switch to any user : {} press 3 {}
                    - Exit the cache manager : {} press 0
        '''.format(TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW))
        #with sr.Microphone() as source:
                 #print("i am listening.....")
                 #m1audio = r.listen(source)
                 #px.speak("sure")
                 #print("sure...")
                 #m = r.recognize_google(m1audio)
                 #print(m)
        m=input()
        if ('exit' in m) or ('quit' in m) or ('close' in m):
            print(TYELLOW, 'Exiting the program ..... ')
            break
        else:
            if (('show' in m) or ('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) and (('available' in m) and ('users' in m)):
                print(
                    TYELLOW, 'Showing the available users  ..... ', TWHITE)
                os.system('cat /etc/passwd ')

            elif (('add' in m) or ('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) and (('new' in m) and ('user' in m)):
                print(TYELLOW, 'Adding a new user ..... ', TWHITE)
                name = input('Enter the name for new user : ')
                os.system('useradd {} '.format(name))

            elif (('switch' in m) or ('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) and (('any' in m) and ('user' in m)):
                print(TYELLOW, 'Switch to any user ..... ')
                name = input(
                    'Enter the name of the user to switch the account : ')
                os.system('su - {} '.format(name))


def aws():
    px.speak("welcome to the aws menu")
    name = input("how do i what to call you!:")
    os.system("clear")
    print("hello \'"+name+"\' \nhow can i help!")
    print()
    print("\t\t\tThis is the menu!\n")
    print("select the following options "+name+"! :\n")
    print("1>AWS instance launch.")
    #with sr.Microphone() as source:
                 #print("i am listening.....")
                 #m1audio = r.listen(source)
                 #px.speak("sure")
                 #print("sure...")
                 #m = r.recognize_google(m1audio)
                 #print(m)
    m=input()

    if (('show' in m) or ('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) and (('instance' in m) and ('launch' in m)):
        print(name+" may i know your credentials so that i can acess your account for this time!")
        s = input("if its ok to you! please enter[y/n]:")
        if s == "y":
            os.system("aws configure")
            print(name+" it's better to create a key pair now,it is useful for ssh")
            keyname = input("enter the keypair name:")
            keycreate = "aws ec2 create-key-pair --key-name --query ""KeyMaterial " + \
                keyname+" --output text > "+keyname+".pem"
            os.system(keycreate)
            print("\n..key hasbeen created and stored in the current working directory..")
            private = "chmod 400 "+keyname+".pem"
            os.system(private)
            enterkey = input(
                "\nEnter the key-pair-name with which you are having:")
            createsys = "aws ec2 run-instances --image-id ami-052c08d70def0ac62 --instance-type t2.micro --key-name "+enterkey
            os.system(createsys)
            os.system("clear")
            print(name+" successfully instance created...")
        elif s == "n":
            print("terminated")
    else:
        print("no")
    print("its done plz check in ur aws site")


def hadoop():
    px.speak("welcome to the hadoop menu")
    print("1>configure name node.\n2>configure data node.\n3>ssh to the aws instance.\n")

    #with sr.Microphone() as source:
                 #print("i am listening.....")
                 #m1audio = r.listen(source)
                 #px.speak("sure")
                 #print("sure...")
                 #m = r.recognize_google(m1audio)
                 #print(m)
    m=input()

    if (('configure' in  m) or ('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) and (('name' in m) and ('node' in m)):
        ipm = input("enter the ipaddress of the name-node:")
        key = input(
            "enter the key associated to the instance, include extension(.pem):")
        ssh = "ssh -i "+key+" ec2-user@"+ipm
        trs = "scp -i "+key
        dirname = input("enter a diretory name for the name-node:")
        h = "<?xml versio=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" herf=\"configuration.xsl\"?>\n<!--put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/" + \
            dirname+"</value>\n</property>\n</configuration>"
        c = "<?xml versio=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" herf=\"configuration.xsl\"?>\n<!--put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://0.0.0.0:9001</value>\n</property>\n</configuration>"
        f = open("hdfs-site.xml", "w")
        f.write(h)
        f.close()
        ff = open("core-site.xml", "w")
        ff.write(c)
        ff.close()
        os.system(trs+" hdfs-site.xml ec2-user@"+ipm+":/home/ec2-user/hdfs-site.xml ;" +
                  trs+" core-site.xml ec2-user@"+ipm+":/home/ec2-user/core-site.xml")
        os.system(ssh+" sudo mv hdfs-site.xml /etc/hadoop/ ;" +
                  ssh+" sudo mv core-site.xml /etc/hadoop/")
        os.system("rm -f hdfs-site.xml core-site.xml")
        os.system("clear")
        print("..the name node at the ip \""+ipm+"\" configured successfully!")
    elif (('configure' in m) or ('open' in m) or ('run' in m) or ('execute'in m) or ('start' in m)) and (('data' in m) and ('node' in m)):
        ipm = input("enter the ipaddress of the name-node:")
        key = input(
            "enter the key associated to the instance, include extension(.pem):")
        ssh = "ssh -i "+key+" ec2-user@"+ipm
        trs = "scp -i "+key
        dirname = input("enter a diretory name for the data-node:")
        h = "<?xml versio=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" herf=\"configuration.xsl\"?>\n<!--put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/" + \
            dirname+"</value>\n</property>\n</configuration>"
        c = "<?xml versio=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" herf=\"configuration.xsl\"?>\n<!--put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://" + \
            ipm+":9001</value>\n</property>\n</configuration>"
        f = open("hdfs-site.xml", "w")
        f.write(h)
        f.close()
        ff = open("core-site.xml", "w")
        ff.write(c)
        ff.close()
        os.system(trs+" hdfs-site.xml ec2-user@"+ipm+":/home/ec2-user/hdfs-site.xml ;" +
                  trs+" core-site.xml ec2-user@"+ipm+":/home/ec2-user/core-site.xml")
        os.system(ssh+" sudo mv hdfs-site.xml /etc/hadoop/ ;" +
                  ssh+" sudo mv core-site.xml /etc/hadoop/")
        os.system("rm -f hdfs-site.xml core-site.xml")
        os.system("clear")
        print("..the data node at the ip \""+ipm+"\" configured successfully!")
    elif (('configure' in m) or ('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) or (('ssh' in m) and ('instance' in m)):
        ipm = input("enter the ipaddress of the instance:")
        key = input("enter the key associated to the instance, include extension(.pem):")
        os.system("clear")
        ssh = "ssh -i "+key+" ec2-user@"+ipm
        os.system(ssh)

    print("......Thank you.......")


def createPV(diskName):
    px.speak("creating a physical volume")
    print(TYELLOW, 'Creating Physical volume')
    print(TBLUE)
    # diskName = input('enter the disk name that you wants to create physical volume(pv): ')
    os.system('pvcreate  {}'.format(diskName))


def createVG(diskName, d1, d2):
    px.speak("creating a volume group")
    print(TYELLOW, 'Creating Volume Group ')
    print(TBLUE)
    # diskName = input('enter the name that you wants to create volume group(vg): ')
    os.system('vgcreate  {} {} {} '.format(diskName, d1, d2))


def displayAllPV():
    px.speak("displaying all the physical volumes available")
    print(TYELLOW, 'Displaying all the physical volumes available ')
    print(TWHITE)
    os.system('pvdisplay ')


def displayAllVG():
    px.speak("displaying the volume groups available")
    print(TYELLOW, 'Displaying all the  volume groups available ')
    print(TWHITE)
    os.system('vgdisplay ')


def displayPV(pvName):
    px.speak("displaying the python volume")
    print(TYELLOW, 'Displaying the physical volume {} '.format(pvName))
    print(TWHITE)
    os.system('pvdisplay  {}'.format(pvName))


def displayVG(vgName):
    px.speak("displaying the volume group")
    print(TYELLOW, 'Displaying the volume group {} '.format(vgName))
    print(TWHITE)
    os.system('vgdisplay  {}'.format(vgName))


def createLV(lvName, vgName, size):
    px.speak("creating the logical volume")
    print(TYELLOW, 'Creating the logical volume ')
    print(TWHITE)
    os.system('lvcreate {} --size {} --name {}'.format(vgName, size, lvName))


def formatt(vgName, lvName):
    px.speak("formating the logical volume")
    print(TYELLOW, 'Formating the logical volume ')
    print(TWHITE)
    os.system('mkfs.ext4 /dev/{}/{} '.format(vgName, lvName))


def extend(size, vgName, lvName):
    px.speak("extending the logical volume")
    print(TYELLOW, 'Extending the logical volume ')
    print(TWHITE)
    os.system('lvextend --size {} /dev/{}/{}'.format(size, vgName, lvName))


def resize(vgName, lvName):
    px.speak("reformatting the logical volume")
    print(TYELLOW, 'Reformatting the logical volume ')
    print(TWHITE)
    os.system('resize2fs /dev/{}/{}'.format(vgName, lvName))


def displayBlocks():
    px.speak("showing the blocks available")
    print(TYELLOW, 'Showing the blocks available ')
    print(TWHITE)
    os.system('lsblk ')


def mounting(vgName, lvName, direc):
    px.speak("mounting the partition to the given directory")
    print(TYELLOW, 'mounting the partition to the given directory ')
    print(TWHITE)
    os.system('mount /dev/{}/{} /{}'.format(vgName, lvName, direc))


def makingDirectory(diskName):
    px.speak("making a new directory")
    print(TYELLOW, 'Making a new directory ')
    print(TWHITE)
    os.system('mkdir {} '.format(diskName))


def disks():
    px.speak("showing available disks")
    print(TYELLOW, 'Showing available disks ')
    print(TWHITE)
    os.system('fdisk -l')


def lvmManager():
    px.speak("welcome to the lvm task")
    while (True):
        px.speak("you are in lvm task menu")
        print(TGREEN)
        print(TGREEN, "\t \t \t Welcome to the LVM Task ")
        print(''' Follow the menu, to perform some task : 
            -> To see the storage devices available : press 1
            -> To create a Physical volume : press 2
            -> To create a Volume group : press 3
            -> To Display the Physical Volumes available : press 4
            -> To display the volume group available : press 5
            -> To display a specific Volume group : press 6
            -> To display a specific Physical volume : press 7
            -> To create a logical volume as per the storage requirements : press 8
            -> To format the logical volume partition : press 9
            -> To extend the space of the logical volume : press 10
            -> To format the unformatted part : press 11
            -> To see the block devices along with their mount point : press 12
            -> To mount the logical volume to some directory, to be used : press 13
            -> To create a directory : press 14
            -> To exit the program : press 0  
        ''')

        print(TBLUE)
        #with sr.Microphone() as source:
                 #print("i am listening.....")
                 #m1audio = r.listen(source)
                 #px.speak("ok")
                 #print("please wait...")
                 #m = r.recognize_google(m1audio)
                 #print(m)
        m=input()

        if ('close' in m) or ('exit' in m) or ('quit' in m):
            print(TYELLOW, 'Exiting from the program ....')
            break

        else:
            print(TYELLOW, 'processing request.....')
            if (('see' or 'open' or 'run' or 'see' or 'start') and ('storage' and 'devices')) in m:
                disks()

            elif (('open' in m) or ('run' in m) or ('create' in m) or ('start' in m)) or (('physical' in m) and ('volume' in m)):
                print(TBLUE)
                diskName = input(
                    'Enter the name of disk that you need to make a physical volume : ')
                createPV(diskName)

            elif (('open' in m) or ('run' in m) or ('create' in m) or ('start' in m)) and (('volume' in m) and ('group' in m)):
                print(TBLUE)
                d1 = input('enter the physical volume to be added : ')
                d2 = input('enter the physical volume to be added : ')
                diskName = input(
                    'Enter the name that you wants to give to your Volume group : ')
                createVG(diskName, d1, d2)

            elif (( 'display' in m) or ('open' in m) or ('run' in m) or ('start' in m)) and (('physical' in m) and ('volume' in m)):
                displayAllPV()

            elif (('display' in m) or ('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) and (('volume' in m) and ('group' in m)):
                displayAllVG()

            elif (('display' in m) or ('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) and (('specific' in m) and ('volume' in m)):
                print(TBLUE)
                vgName = input(
                    'Enter the volume group name that you wants to retrieve  : ')
                displayVG(vgName)

            elif (('display' in m) or ('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) and (('specific' in m) and ('docker' in m)):
                print(TBLUE)
                pvName = input(
                    'Enter the physical volume name that you wants to retrieve  : ')
                displayPV(pvName)

            elif (('create' in m) or ('open' in m) or ('run' in m) or ('start' in m)) and (('storage' in m) and ('requirements' in m)):
                print(TBLUE)
                vgName = input('Enter the volume group name : ')
                size = input('Enter the size of logical device you want : ')
                lvName = input(
                    'Enter the name of your choice for Logical volume : ')
                createLV(lvName, vgName, size)

            elif (('format' in m) or ('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) and (('logical' in m) and ('volume' in m)):
                print(TBLUE)
                vgName = input('Enter the volume group name : ')
                lvName = input('Enter the Logical volume name : ')
                formatt(vgName, lvName)

            elif (('extend' in m) or ('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) and (('space' in m) and ('logical'  in m)):
                print(TBLUE)
                vgName = input('Enter the volume group name : ')
                size = input('Enter the size to be extended : ')
                lvName = input('Enter the Logical volume name : ')
                extend(size, vgName, lvName)

            elif (('format' in m) or ('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) and (('unformatted' in m) and ('part' in m)):
                print(TBLUE)
                vgName = input('Enter the volume group name : ')
                lvName = input('Enter the Logical volume name : ')
                resize(vgName, lvName)

            elif (('see' in m) or ('display' in m) or ('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) and (('block' in m) and ('devices' in m)):
                displayBlocks()

            elif (('mount' in m) or ('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) and (('logical' in m) and ('volume' in m)):
                print(TBLUE)
                vgName = input('Enter the volume group name : ')
                lvName = input('Enter the Logical volume name : ')
                direc = input(
                    'Enter the directory name to be linked with this Logical volume :')
                mounting(vgName, lvName, direc)

            elif (('to' in m) or ('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) and (('create' in m) and ('directory' in m)):
                print(TBLUE)
                diskName = input(
                    'Enter the name for the directory that you wants to create : ')
                makingDirectory(diskName)

            else:
                px.espeak("say it clearly..")
                print(TRED, 'Enter valid options only !!!')
                continue


def docker():
    px.speak("welcome to the docker manageer menu")
    while (True):
        print(TGREEN, '\t \t Welcome to the Docker Manager \n  ')
        px.speak("you are in docker manager menu")
        print('''  \t List of operations that can be performed with Docker Manager :- 
                    - Install Docker : {} press 1 {}
                    - Show the list of docker images : {} press 2 {}
                    - Pull a docker image : {} press 3 {}
                    - Create a docker container : {} press 4 {}
                    - Start a docker : {} press 5 {}
                    - Go inside a docker : {} press 6 {}
                    - Setup webServer over docker : {} press 7 {}  
                    - check the docker status : {} press 8 {}        
                    - Exit the cache manager : {} press 0        
        '''.format(TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW))
        #with sr.Microphone() as source:
                 #print("i am listening.....")
                 #m1audio = r.listen(source)
                 #px.speak("sure")
                 #print("sure...")
                 #m = r.recognize_google(m1audio)
                 #print(m)
        m=input()
        if ('close' in m) or ('exit' in m) or ('quit' in m):
            print(TYELLOW, 'Exiting the program ..... ')
            break
        else:
            if (('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) or (('install' in m) and ('docker' in m)):
                print(TYELLOW, 'Installing  Docker  ..... ', TWHITE)
                os.system('yum install git -y')
                os.system('mkdir /dockerRepo')
                os.system(
                    'git clone https://github.com/Anshika-Sharma-as/docker-repo.git /dockerRepo')
                os.system(
                    'cp /dockerRepo/docker.repo  /etc/yum.repos.d/docker.repo ')
                os.system('rm -f /dockerRepo')
                os.system('yum install docker-ce --nobest -y')
                os.system('systemctl start docker')

            elif (('show' in m) or ('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) or (('list' in m) and ('docker' in m)):
                print(TYELLOW, 'Showing the list of docker images ..... ', TWHITE)
                os.system('docker images ')

            elif (('open' in m) or ('run' in m) or ('execute'  in m) or ('start' in m) or ('pull' in m) and ('docker' in m)):
                print(TYELLOW, 'Pulling a docker image ..... ', TWHITE)
                imageName = input('Enter the name of docker image : ')
                os.system('docker pull {} '.format(imageName))

            elif (('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m))  or (('create' in m) and ('docker' in m)):
                print(TYELLOW, 'Creating a docker container ..... ', TWHITE)
                name = input('Enter the name for docker container : ')
                imageName = input('Enter the name of docker image : ')
                os.system(
                    'docker run -dit --name {}  {}'.format(name, imageName))
                os.system('docker ps -a')

            elif (('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) and ('docker' in m):
                print(TYELLOW, 'Starting a docker  ..... ', TWHITE)
                name = input('Enter the name of Container to be started : ')
                os.system('docker start {} '.format(name))
                os.system('docker ps ')

            elif (('configure' in m) or ('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) or (('inside' in m) and ('docker' in m)):
                print(TYELLOW, 'Going inside a docker ..... ', TWHITE)
                name = input('Enter the name of Container to be started : ')
                os.system('docker exec -it {} /bin/bash '.format(name))

            elif (('configure' in m) or ('open'  in m) or ('run' in m) or ('execute' in m) or ('start' in m)) or (('setup' in m) and ('webserver' in m)):
                print(TYELLOW, 'Setup webServer over docker ..... ', TWHITE)
                name = input(
                    'Enter the name of Container to perform operations : ')
                os.system('docker start {}'.format(name))
                os.system(
                    'docker exec -dit {} yum install httpd -y'.format(name))
                os.system('docker exec -dit {} /usr/sbin/httpd'.format(name))
                os.system('docker exec -dit {} mkdir /dockerRepo'.format(name))
                os.system('docker exec -dit {} yum install git -y'.format(name))
                os.system(
                    'docker exec -dit {} git clone https://github.com/Anshika-Sharma-as/docker-repo.git /dockerRepo'.format(name))
                os.system(
                    'docker exec -dit {} cp /dockerRepo/web.html /var/www/html'.format(name))
                print('Access your web page on below IP : ')
                os.system('docker exec -dit {} ifconfig'.format(name))
                print('http://IP_Address/web.html')
                ip = input('Enter the IP to access the webserver : ')
                os.system('http://{}/web.html'.format(ip))

            elif (('check' in m) or ('open' in m) or ('run' in m) or ('execute' in m) or ('start' in m)) and (('docker' in m) and ('status' in m)):
                print(TYELLOW, 'Checking the docker status ..... ', TWHITE)
                os.system('systemctl status docker ')

            else:
                px.speak("say it clear")
                print(TYELLOW, 'Choose a valid option !!!', TWHITE)
                continue

        print(TBLUE, '\n ')
        cont = input(
            'Do you wants to continue with the Docker Manager ?[y/n] : ')
        if (cont == 'y') or (cont == 'Y'):
            continue
        else:
            break


def mainMenu():
    while(True):
        if status == 1:
            px.speak("here is the main menu")
            print(TGREEN, '''\n List of every operation, choose anyone to process:-
                -  About my system :  press 1 
                -  Manage my AWS Cloud remotely : {} press 2 {}
                -  Setup and Manage Hadoop Cluster : {} press 3 {}
                -  Manage multiple programs at single time : {} press 4 {}
                -  Managing users in the system : {} press 5 {}
                -  Use File Manager Program : {} press 6 {}
                -  Check connections with other systems : {} press 7 {}
                -  Use Binary Calculator : {} press 8 {}
                -  Managing Cache memory : {} press 9 {}
                -  Manage background processes : {} press 10 {}
                -  Manage Containers through Docker : {} press 11 {}
                -  Managing storage :{} press 12 {}
                -  Exit the program : {} press 0 

            '''.format(TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW))

            #with sr.Microphone() as source:
                 #print("Assistant: i am listening.....")
                 #m1audio = r.listen(source)
                 #px.speak("ok")
                 #print("Assistant: please wait...")
                 #m1txt = r.recognize_google(m1audio)
                 #print("me: "+m1txt)
            m1txt=input()
            if (('exit' in m1txt) or ('close' in m1txt) or ('quit' in m1txt)):
                print(TYELLOW, 'Exiting the program .....')
                break
            else:
                if (('open' in m1txt) or ('run' in m1txt) or ('execute' in m1txt) or ('about' in m1txt)) and (('about' in m1txt) and ('system' in m1txt)):
                    print('Opening about the system .....')
                    aboutSystem()

                elif (('open' in m1txt) or ('run' in m1txt) or ('execute' in m1txt) or ('start' in m1txt)) and (('manage' in m1txt) and (('aws' in m1txt) or ('cloud' in m1txt))):
                    print('managing AWS cloud .....')
                    aws()

                elif (('open' in m1txt) or ('run' in m1txt) or ('execute' in m1txt) or ('start' in m1txt)) and (('hadoop' in m1txt) and ('setup'in m1txt)):
                    print('Opening Hadoop Manager .....')
                    hadoop()

                elif (('open' in m1txt) or ('run' in m1txt) or ('execute' in m1txt) or ('start' in m1txt)) and (('manage' in m1txt) and ('multiple' in m1txt)):
                    print('Opening Multi program setup .....')
                    manageMultipleProgram()

                elif (('open' in m1txt) or ('run' in m1txt)  or ('execute' in m1txt) or ('start' in m1txt)) and (('managing' in m1txt) and ('users' in m1txt)):
                    print('Opening user management program  .....')
                    userManager()

                elif (('open' in m1txt) or ('run' in m1txt) or ('execute' in m1txt) or ('start' in m1txt)) and (('file' in m1txt) and ('manager' in m1txt)):
                    print('Opening file manager program .....')
                    fileManager()

                elif (('open' in m1txt) or ('run' in m1txt) or ('execute' in m1txt) or ('start' in m1txt)) and (('check' in m1txt) and ('connection' in m1txt)):
                    print('Opening connection checker .....')
                    connectionChecker()

                elif (('open' in m1txt) or ('run' in m1txt) or ('execute' in m1txt) or ('start' in m1txt)) and (('binary' in m1txt) and ('calculator' in m1txt)):
                    print('Opening Binary calculator .....')
                    binaryCalulator()

                elif (('open' in m1txt) or ('run' in m1txt) or ('execute' in m1txt) or ('start' in m1txt)) and (('cache' in m1txt) and ('memory' in m1txt)):
                    print('Opening cache Manager .....')
                    cacheManager()

                elif (('open' in m1txt) or ('run' in m1txt) or ('execute' in m1txt) or ('start' in m1txt)) and (('background' in m1txt) and ('process' in m1txt)):
                    print('Opening Background process Manager .....')
                    processManager()

                elif (('open' in m1txt) or ('run' in m1txt) or ('execute' in m1txt) or ('start' in m1txt)) and ('docker'in m1txt):
                    print('Opening Docker Manager .....')
                    docker()

                elif (('open' in m1txt) or ('run' in m1txt) or ('execute' in m1txt) or ('start' in m1txt)) and (('managing' in m1txt) and ('storage' in m1txt)):
                    print('Opening Storage Manager .....')
                    lvmManager()

                else:
                    px.speak("sorry try again")
                    print('Assistant: Choose a valid option !!!')
                    continue

            print(TGREEN, '\n \n ')
            px.speak("do you whant to continue with command assistant")
            cont = input('Do you wants to continue with the Command Assistant ?[y/n] : ')
            if (cont == 'y') or (cont == 'Y'):
                continue
            else:
                break


mainMenu()
print(TGREEN, '\t \t Execution Done !! ', TWHITE)
