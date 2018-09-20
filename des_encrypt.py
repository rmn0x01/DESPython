#Data Encryption Standard
#rmn0x01

def circularShiftLeft(binaries,shift): #geser biner sesuai total shift
	cut=binaries[:shift]
	res=binaries[shift:]+cut
	return res

def keyGenerator(key): #menghasilkan semua key sesuai algoritma yang sudah ditentukan
	permutation_choice_1=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
	permutation_choice_2=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
	shift = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
	binaries=''
	for i in key:
		if (len(bin(ord(i))[2:])==8):
			binaries+=bin(ord(i))[2:]
		else:
			binaries+=(8 - len(bin(ord(i))[2:]) % 8)*'0'+bin(ord(i))[2:]
	tmp = ['a' for i in range(56)]
	temp = ['a' for i in range(48)]
	for i in range(len(permutation_choice_1)):
		tmp[i] = binaries[permutation_choice_1[i]-1]
	pcs_1 = str(''.join(tmp))
	c = pcs_1[:28]
	d = pcs_1[28:]
	for i in range(16):
		c=circularShiftLeft(c,shift[i])
		d=circularShiftLeft(d,shift[i])
		pcs_1=c+d
		for j in range(len(permutation_choice_2)):
			temp[j] = pcs_1[permutation_choice_2[j]-1]
		pcs_2=str(''.join(temp))
		list_of_key[i]=pcs_2
		

def initialPermutation(binaries): #permutasi awal
	initial_permutation =[58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
	result = ['a' for i in range(64)]
	for i in range(len(initial_permutation)):
		result[i] = binaries[initial_permutation[i]-1]
	res = str(''.join(result))
	return res

def finalPermutation(binaries): #permutasi akhir
	final_permutation =[40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]
	result = ['a' for i in range(64)]
	for i in range(len(final_permutation)):
		result[i] = binaries[final_permutation[i]-1]
	res = str(''.join(result))
	return res

def sBox(binaries): #substitusi dengan SBox
	sbox1 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
	sbox2 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
	sbox3 = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]
	sbox4 = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]
	sbox5 = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]
	sbox6 = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]
	sbox7 = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
	sbox8 = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
	sbox=[sbox1,sbox2,sbox3,sbox4,sbox5,sbox6,sbox7,sbox8]
	result=''	
	for i in range(0,len(binaries),6):
		tmp = binaries[i:i+6]
		row = int(tmp[0]+tmp[5],2)
		col = int(tmp[1:5],2)
		temp = bin(sbox[i/6][row][col])[2:]
		if(len(temp)==4):
			result+=temp
		else:
			result+=(4-len(temp)%4)*'0'+temp
	return result

def feistel(binaries,rounds): #Feistel cipher, inti dari DES
	expansion_table = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
	straight_permutation_table = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]
	expanded = ['a' for i in range(48)]
	for i in range(len(expansion_table)):
		expanded[i] = binaries[expansion_table[i]-1]
	expanded_binaries = str(''.join(expanded))
	tmp=''	
	for i in range(len(expanded_binaries)):
		tmp+=str(ord(expanded_binaries[i])^ord(list_of_key[rounds][i]))
	temp = sBox(tmp)
	res = ['a' for i in range(32)]
	for i in range(len(straight_permutation_table)):
		res[i] = temp[straight_permutation_table[i]-1]
	result = str(''.join(res))
	return result

def DES(text): #menghandle plaintext masuk, looping 16 kali, mengembalikan ciphertext
	binaries=''
	for i in text:
		if (len(bin(ord(i))[2:])==8):
			binaries+=bin(ord(i))[2:]
		else:
			binaries+=(8 - len(bin(ord(i))[2:]) % 8)*'0'+bin(ord(i))[2:]
	binaries=initialPermutation(binaries)
	left = binaries[:32]
	right = binaries[32:]
	for i in range(16):
		temp_right = right
		right = feistel(right,i)
		right2 = ''
		for j in range(len(right)):
			right2+=str(ord(left[j])^ord(right[j]))
		left = temp_right
		right = right2
	final = right+left
	result = finalPermutation(final)
	return result

list_of_key = ['' for x in range(16)] #menyimpan ke-16 key yang sudah di-generate
list_of_plaintext = ['' for x in range(100)] #menyimpan blok - blok plaintext apabila lebih dari 8 karakter
print "Input plaintext: "
plaintext = raw_input()
print "Input key (8 characters): "
key = raw_input()
keyGenerator(key)
if (len(plaintext)%8!=0): #padding
	plaintext += (8 - len(plaintext) % 8)*' '
for i in range(0,len(plaintext),8):
	list_of_plaintext[i/8] = plaintext[i:i+8]

ciphertext=''
for i in range(len(plaintext)/8):
	tmp = DES(list_of_plaintext[i])
	for j in range(0,len(tmp),8):
		ciphertext+=chr(int(tmp[j:j+8],2)) #menggabungkan hasil DES tiap blok ke satu string ciphertext utuh

print "Ciphertext: " + ciphertext
print "Ciphertext hex encoded: "+ ciphertext.encode('hex')
