#!/usr/bin/env python
# coding: utf-8

# In[6]:


def encrypt(key,plaintext):
    ciphertext=""
    #YOUR CODE HERE
    # transverse the plain text
    for i in range(len(plaintext)):
      char = plaintext[i]
      # Encrypt uppercase characters in plain text
      ciphertext += chr((ord(char) + key-65) % 26 + 65)
    return ciphertext


# In[9]:


def decrypt(key,ciphertext):
    plaintext=""
    #YOUR CODE HERE
    # transverse the cipher text
    for i in range(len(ciphertext)):
      char = ciphertext[i]
      # Decrypt uppercase characters in cipher text
      plaintext += chr((ord(char) - key-65) % 26 + 65)
    return plaintext


# In[18]:


plaintext = "CEASER"
key = 27


print("Plain Text : " + plaintext)
print("Shift pattern : " + str(key))
print("Cipher: " + encrypt(key,plaintext))


# In[19]:


ciphertext = "DFBTFS"
key = 27

print("cipher Text : " + ciphertext)
print("Shift pattern : " + str(key))
print("Cipher: " + decrypt(key,ciphertext))


# In[ ]:




