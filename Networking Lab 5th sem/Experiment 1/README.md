# Experiment 1: Implement and Analyze Classical Symmetric Ciphers

## Objective
To implement and analyze classical symmetric ciphers (Caesar and Vigenère) for encryption and decryption using Python.

## Procedure

### A. Caesar Cipher
1.  Open Python 3 in VS Code and run the Caesar cipher program.
2.  Provide the plaintext and required shift value as input from the user.

> [**View Ceaser_ciper Code**](Code/Caesar_cipher.py)
> 
![alt text](Outputs/Caesar.png)
> **Ceaser_ciper Output 1 - Encryption**

3.  The program encrypts the plaintext using a fixed shift with modulo 26 logic, while preserving spaces, numbers and punctuation as they are.
4.  The ciphertext is then decrypted using the reverse shift logic and compared with the original plaintext to verify correctness.

> **Ceaser_ciper Output 2 - Decryption & Verification**

### B. Vigenere Cipher
1.  Run the Vigenère cipher program and provide the plaintext and an alphabetic key as input.

> [**View Vignere_cipher Code**](Code/vignere.py)
> 
![alt text](Outputs/vignere.png)


> **Vignere_cipher Code Output 1 - Encryption**

2.  The program encrypts the plaintext using the repeating key method, preserving spaces and punctuation without advancing the key position.
3.  The ciphertext is decrypted using the same key and the result is compared with the original plaintext for verification.

> **Vignere_cipher Output 2 - Decryption & Verification**

4.  Multiple test cases for both ciphers are executed to verify that the decrypted messages match the original messages.

## Result
The Caesar and Vigenère cipher programs were successfully implemented and executed in Python. Both programs performed encryption and decryption correctly. All 4 test cases produced correct round-trip results, giving a 100% verification success rate.

## Discussion
Both ciphers successfully performed encryption and decryption, with the decrypted messages matching exactly with the original plaintexts in all test cases.

The Caesar cipher uses a single fixed shift for the entire message. This makes it very simple and easy to implement, but it is highly vulnerable to security attacks. Since there are only 25 possible keys, it can be easily broken by a Brute-Force Attack. It is also vulnerable to Frequency Analysis because the same plaintext letter always becomes the same ciphertext letter.

The Vigenère cipher is an improvement over the Caesar cipher. It uses a repeating keyword with different shift values, so the same plaintext letter is encrypted to different ciphertext letters. This reduces simple letter frequency patterns and makes it more secure than Caesar cipher. However, when sufficient ciphertext is available, it can still be attacked using methods like Kasiski Examination to find the key length.

## Improvements

**Caesar Cipher:** Modified the program to accept plaintext and shift value from the user instead of using fixed values.
**Vigenère Cipher:** Modified the program to accept plaintext and key from the user, making it interactive.

## Conclusion
Thus, Caesar and Vigenère ciphers were successfully implemented in Python and verified through various test cases. This experiment helped in understanding the basic working of classical symmetric encryption techniques, their implementation logic using modulo arithmetic, and their security limitations compared to modern encryption algorithms.
