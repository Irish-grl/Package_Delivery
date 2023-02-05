#-----------------------------------------------------------------------------------------------------------------------
# Author: Jessica Thomas
# WGUPS Package Delivery Project
#
#-----------------------------------------------------------------------------------------------------------------------

import csv

#-----------------------------------------------------------------------------------------------------------------------
#  Function finds the next nearest location and drops package(s)
#-----------------------------------------------------------------------------------------------------------------------
class HashFunctions:

    #constructor for the delivery truck hash tables
    def __init__(self, hub = 40):

        #creates table of lists
        self.table = []

        #adds list to each index of the table
        for i in range(hub):
            self.table.append([])

    def insert(self, key, packageId):

        #discern where in the table the package should be inserted
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        #add the package into the list
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] == packageId
                return True

        key_value = [key, packageId]
        bucket_list.append(key_value)
        return True

    def find(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if key in kv:
                return kv[1]


#-----------------------------------------------------------------------------------------------------------------------
#  Function finds the next nearest location and drops package(s)
#-----------------------------------------------------------------------------------------------------------------------
class Truck:

    def __init__(self, tId, max_packages = 16, start_time = None):
        self.tId = tId
        self.max_packages = max_packages
        self.start_time = start_time
        self.max_distance = 0
        self.package_list = []

    def insert(self, aId):
        self.package_list.append(aId)
        return


#-----------------------------------------------------------------------------------------------------------------------
#  Function finds the next nearest location and drops package(s)
#-----------------------------------------------------------------------------------------------------------------------
class Addresses:

    list = []
    def __init__(self, id, address):

        self.id = id
        self.address = address
        self.list = []

    with open('Addresses.csv', 'r') as addresses:
        address_data = csv.reader(addresses, delimiter=',')
        for a in address_data:
            aId = a[0]
            aAddress = a[1]

            a = (aId, aAddress.strip(' '))
            list.append(a)


#-----------------------------------------------------------------------------------------------------------------------
#  Function finds the next nearest location and drops package(s)
#-----------------------------------------------------------------------------------------------------------------------
class Distances:

    distance_object = {}
    def __init__(self, id, miles):
        self.id = id
        self.miles = miles
        self.distance_object = self.distance_object

    with open('Distances.csv', 'r') as distance:
        distance_data = csv.reader(distance, delimiter=',')
        for d in distance_data:
            distance_object[int(d[0])] = d

#-----------------------------------------------------------------------------------------------------------------------
#  Function finds the next nearest location and drops package(s)
#-----------------------------------------------------------------------------------------------------------------------
class Package:

    def __init__(self, id, address, city, state, zip, delivery_req, weight, inst, truck = None, delivery_time = None):

        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.weight = weight
        self.delivery_req = delivery_req
        self.inst = inst
        self.truck = truck
        self.delivery_time = delivery_time
        self.distance = 0.0
        self.list = []

    def __str__(self):  # overwrite print(Package) otherwise it will print object reference instead

        return "%d, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.id, self.address, self.city, self.state, self.zip, self.weight, self.inst, self.delivery_time,
            self.truck, self.delivery_req)

    pkg_table = HashFunctions()
    with open('Packages.csv', 'r') as packages:
        package_data = csv.reader(packages, delimiter=',')
        for pkg in package_data:
            pId = int(pkg[0])
            pAddress = pkg[1]
            pCity = pkg[2]
            pState = pkg[3]
            pZip = pkg[4]
            pDelivery = pkg[5]
            pWeight = pkg[6]
            pInst = pkg[7]

            p = (pId, pAddress, pCity, pState, pZip, pDelivery, pWeight, pInst)  # package object
            pkg_table.insert(pId, p) # insert packages into the 'hub'.

#-----------------------------------------------------------------------------------------------------------------------
#  Function finds the next nearest location and drops package(s)
#-----------------------------------------------------------------------------------------------------------------------

def fill_trucks(truck_1, truck_2, truck_3):
    pkg_id_list_truck_1 = [16, 38, 12, 11, 10, 9, 28, 6, 39, 3, 32, 1, 0]
    pkg_id_list_truck_2 = [35, 22, 21, 20, 19, 18, 17, 33, 15, 14, 13, 37, 36, 4, 2]
    pkg_id_list_truck_3 = [31, 30, 27, 34, 26, 25, 24, 23, 29, 8, 7, 5]

    pkg_data = []
    for this_pkg_id in pkg_id_list_truck_1:
        pkg_data = packages.find(this_pkg_id)
        truck_1.package_list.append(pkg_data)
    for this_pkg_id in pkg_id_list_truck_2:
        pkg_data = packages.find(this_pkg_id)
        truck_2.package_list.append(pkg_data)
    for this_pkg_id in pkg_id_list_truck_3:
        pkg_data = packages.find(this_pkg_id)
        truck_3.package_list.append(pkg_data)

distances = Distances().distance_object
addresses = Addresses().list
packages = Package().pkg_table
