#code above below us to access every number the user inputs in the format
#.#.#.#/#
userinput = input('Enter IPv4 Address and submask in the form #.#.#.#/#: ').split('/')
first_half = userinput[0]
submask = userinput[1]

octets = first_half.split('.')

octets.append(submask)


#now convert octets to integers

int0 = int(octets[0])
int1 = int(octets[1])
int2 = int(octets[2])
int3 = int(octets[3])

#now convert them to binary and to always be in 8 bit

b0 = format(int0, '08b')
b1 = format(int1, '08b')
b2 = format(int2, '08b')
b3 = format(int3, '08b')


#now add binaries together as one string

binaries = b0 + b1 + b2 + b3

#now replace every binary with the number 1 after the nth digit
intsubmask = int(submask)
broadcast_address = binaries[:intsubmask]  + '1' *(len(binaries) - intsubmask)

#convert string back into #.#.#.#/# format
octet0 = broadcast_address[:8]
octet1 = broadcast_address[8:16]
octet2 = broadcast_address[16:24]
octet3 = broadcast_address[24:32]


a =int(octet0,2) 
b = int(octet1,2) 
c = int(octet2,2)
d = int(octet3,2)



broadcast_address_complete = str(a) + "." + str(b) + "." + str(c) + "." + str(d)

print('This is ur Broadcast Address:', broadcast_address_complete)

#now, time to code for the network address, 

#take the binaries, everything after the n'th digit  into 0's 

network_address = binaries[:intsubmask]  + '0' *(len(binaries) - intsubmask)

octet0a = network_address[:8]
octet0b = network_address[8:16]
octet0c = network_address[16:24]
octet0d = network_address[24:32]

a1 = int(octet0a,2)
b1 = int(octet0b,2)
c1 = int(octet0c,2)
d1= int(octet0d,2)


network_address_complete = str(a1) + "." + str(b1) + "." + str(c1) + "." + str(d1) + '/' + submask

print('This is ur network address:', network_address_complete)

#now for range of host addresses
#add 1 to the end of the netwrok address binaries to fund the first host address

network_address_binaries_plus_one = network_address[:-1] + '1'



#turn them back into base 10

octet1a = network_address_binaries_plus_one[:8]
octet1b = network_address_binaries_plus_one[8:16]
octet1c = network_address_binaries_plus_one[16:24]
octet1d = network_address_binaries_plus_one[24:32]

a2 = int(octet1a,2)
b2 = int(octet1b,2)
c2 = int(octet1c,2)
d2 = int(octet1d,2)

network_address_add_one_complete = str(a2) + "." + str(b2) + "." + str(c2) + "." + str(d2)

#now time for the broadcast address
#subtract one to the end of the broadcast address to find the last host address

broadcast_address_binaries_sub_one = broadcast_address[:-1] + '0'


#turn them back into base 10

octet2a = broadcast_address_binaries_sub_one[:8]
octet2b = broadcast_address_binaries_sub_one[8:16]
octet2c = broadcast_address_binaries_sub_one[16:24]
octet2d = broadcast_address_binaries_sub_one[24:32]

a3 = int(octet2a,2)
b3 = int(octet2b,2)
c3 = int(octet2c,2)
d3 = int(octet2d,2)

broadcast_address_sub_one_complete = str(a3) + "." + str(b3) + "." + str(c3) + "." + str(d3)

#now print them 

print('ur range of hosts is from ', network_address_add_one_complete, 'to' , broadcast_address_sub_one_complete)


