import os  
def yum_configure():
    try:
        os.system("cp epel.repo dock.repo  epel-playground.repo epel-testing.repo root.repo rpmfusion-free-updates.repo rpmfusion-free-updates-testing.repo /etc/yum.repos.d/ ")
        print("Your yum is configured now check it by 'yum repolist' command. ")
        c=input("Press Enter to continue...")
    except ValueError:
        print("Error ...... Please try later...")
        c=input("Press Enter to continue...")
    
def docker_installation():
    try:
        os.system("yum install docker-ce --nobest -y")
        print("Docker sucessfully installed....")
        c=input("Press Enter to continue...")
    except ValueError:
        print("Error ...... Please try later...")
        c=input("Press Enter to continue...")

def change_reso():
    try:
        os.system("yum install make perl -y")
        os.system("yum install kernel-devel -y")
        os.system("yum install elfutils-libelf-devel -y")
        print(""" Now follow following steps:
            step 1: unmount your rhel-dvd.
            step 2: Now go to devices in vm menu bar.
            step 3: Now select option "Insert guest additions cd image..."
            step 4: Now a new cd mounted on your os and a dialog come with run and cancel option.
            step 5: Now select run. let the setup done. it will take some minutes.
            step 6: Now wait till its show "press return to close this window..."
            step 7: Now unmount that cd and again mount rhel CD.

            Hurrey..... then your problem solved. Thanks...
            """)	
        b=input("press Enter to continue key")
    except ValueError:
        print("Error ...... Please try later...")
        c=input("Press Enter to continue...")

def infra_setup(a):
    if a==4:
        flag=0
        try:
            os.system(' curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
            os.system("chmod +x /usr/local/bin/docker-compose")
            os.system("cp docker-compose.yml /") 
            os.system("cd / ")
            os.system("mkdir /my_infrastructure")
            os.system("cd /my_infrastructure/")
            os.system("pwd")
            os.system("mv ../docker-compose.yml .")
            os.system("docker-compose up -d")
        except ValueError:
            print("Error .... Watch tutorial .... to solve this.")
            x=input("Press Enter to continue....")
            flag=1
        if flag == 0 :
            print("\n\n     Now access your wordpress site by redhat IP:8081  < eg:- 123.456.789.12:8081 > in your redhat firefox.")
            x=input("Press Enter to continue...")

    elif a==5:
        os.system("docker-compose up -d")
        print("\n\n     Now access your wordpress site by redhat IP:8081  < eg:- 123.456.789.12:8081 > in your redhat firefox.\n    or visit tutorial videos")
        x=input("Press Enter to continue...")

    
    elif a==6:
        os.system("docker pull centos:7")
        os.system("firewall-cmd --zone=public --add-masquerade --permanent")
        os.system("firewall-cmd --zone=public --add-port=80/tcp")
        os.system("firewall-cmd --zone=public --add-port=443/tcp")
        os.system("firewall-cmd --reload")
        os.system("systemctl restart docker")
        print("\n\n Now your problem is solved. Enjoy ......")
        x=input("Press Enter to continue...")



        



    


while True:
    os.system("clear")
    print(""" 
    
                              Main Menu
                              =========

  Press following keys to proceed :

  1. Basic Yum Configuration            ( atleast 15 mb internet data required )
  2. Full Size Screen Resolution in Redhat 8      (atleast 50 mb internet data  required.)
  3. Docker Installation                (in only Red Hat, atleast 200 mb internet data required.)
  4. Installation of WordPress Site     (with Database)  <atleast 500 mb internet data required>
  5. Reconstruct Infrastruture          (if website crashed within few seconds)
  6. Centos:7 yum error solution        < first watch tutorial video

Note : First visit tutorial video as in video directory.

  9. Exit
            
            
  Enter your option : """,end='')

    ch = input()

    try : 
        choice= int(ch)
    except ValueError:
        print("\n\n Invalid Input...... Press again")
        x=input("Press Enter to continue...")
        continue

    if(choice==1):
        yum_configure()
        continue
    elif(choice==3):
        docker_installation()
        continue
    elif(choice==2):
        change_reso()
        continue
    elif(choice==4):
        infra_setup(choice)
        continue

    elif(choice==5):
        infra_setup(choice)
        continue
    elif(choice==6):
        infra_setup(choice)
        continue

    elif(choice==9):
        exit(0)
    else:
        print("INvalid Input..... Please Enter again..")
        x=input("Press Enter to continue...")
