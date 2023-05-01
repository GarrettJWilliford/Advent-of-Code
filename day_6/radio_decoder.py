import radio_packet as rp

#Part 1
def find_marker(packet):
	for i in range(len(packet)):
		try:
			current_packet = packet[i:i+4]
		except:
			return -1
		if len(set(current_packet)) == 4:
			return i+4


#Check
print('Marker Location: ' + str(find_marker(rp.packet_1)))



#Part 2
def find_message_marker(packet):
	for i in range(len(packet)):
		try:
			current_packet = packet[i:i+14]
		except:
			return -1
		if len(set(current_packet)) == 14:
			return i+14


print('Marker Location: ' + str(find_message_marker(rp.packet_1)))
