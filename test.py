import netmiko
import sys
import os

host = "192.168.43.1"
login_device = "admin"
pass_device = "passwd"
device = "cisco_ios"
int_num = 0

# CONNECTION
conn = netmiko.ConnectHandler(ip=host, device_type=device, username=login_device, password=pass_device)

# COICE TO CONFIGURE INTERFACE OR BGP

while True:
  choice = input("what do you want to configure? interface - 1 | bgp - 2 : ")

  while choice != "0":
    # FUNCTION TO CONFIGURE INTERFACE
    def basicConf():
      count = 0
      int_num = input("how many interface : ")
      if int_num != "0":
        while int(int_num) > count:
          interface = input("Interface : ")
          ipAddr = input("ip :")
          mask = input("mask :")

          conf_bsc = ["int " + interface,
                      "ip add " + ipAddr + " " + mask,
                      "no shut",
                     ]

          print(conn.send_config_set(conf_bsc))
          count+=1
      else:
        re = sys.executable
        os.execl(re, re, *sys.argv)
        #sys.exit()


    # FUNCTION TO CONFIGURE BGP
    def bgpConf():
      count1 = 0
      count2 = 0
      bgp = input("router bgp : ")
      if bgp != "0":
        n_num = input("number of neighbour(s) : ")
        net_num = input("number of network : ")

        if n_num != "0":
          while int(n_num) > count1:
            neighbor = input("enter neighbor : ")
            rem_as = input("enter AS : ")
            conf_bgp = ["router bgp " + bgp,
                        "neighbor " + neighbor + " remote-as " + rem_as,
                       ]
            print(conn.send_config_set(conf_bgp))
            count1+=1
        else:
          print("proceed with network")

        if net_num != "0":
          while int(net_num) > count2:
            net = input("enter network : ")
            mask1 = input("enter mask : ")
            conf_bgp1 = ["router bgp " + bgp,
                         "network " + net + " mask " + mask1,
                        ]
            print(conn.send_config_set(conf_bgp1))
            count2+=1
        else:
          re = sys.executable
          os.execl(re, re, *sys.argv)
      else:
        re = sys.executable
        os.execl(re, re, *sys.argv)
        #sys.exit()

    # FUNCTION TO SHOW
    def show():
      print(conn.send_command("sh ip int br"))


    # CONDITION FOR CHOICE
    if choice ==  "1":
      basicConf()

    elif choice == "2":
      bgpConf()

    else:
      print("INVALID OPTION!!")
      show()
      conn.disconnect()
      sys.exit()

conn.disconnect()
