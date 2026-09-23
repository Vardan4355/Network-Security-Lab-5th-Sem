Lab Manual: Generating an X.509 Self-Signed Digital Certificate
Objective

To generate a private key and create an X.509 self-signed digital certificate using OpenSSL.
Requirements

    OpenSSL installed on your system
    Command-line terminal
    Basic knowledge of file paths and commands

Theory

An X.509 certificate binds an identity, such as a domain name, to a public key. A self-signed certificate is signed using its own private key instead of a certificate authority. It is useful for laboratories, development, testing, and internal systems.

The generated files are:

    private.key — private key
    certificate.crt — self-signed X.509 certificate

Procedure
1. Verify OpenSSL installation

Open a terminal and run:
bash

openssl version

If OpenSSL is installed, its version will be displayed.
2. Create a working directory
bash

mkdir openssl-labcd openssl-lab

3. Generate the private key

Generate a 2048-bit RSA private key:
bash

openssl genpkey -algorithm RSA \  -out private.key \  -pkeyopt rsa_keygen_bits:2048

Confirm that the file was created:
bash

ls -l private.key

On Windows, use:
cmd

dir private.key

4. Protect the private key

On Linux or macOS, restrict access to the private key:
bash

chmod 600 private.key

The private key must not be shared with other users.
5. Generate the self-signed certificate

Run:
bash

openssl req -x509 -new -sha256 -days 365 \  -key private.key \  -out certificate.crt

Enter the requested information. Example values:
text

Country Name: USState or Province Name: CaliforniaLocality Name: Los AngelesOrganization Name: Example OrganizationOrganizational Unit Name: IT DepartmentCommon Name: localhostEmail Address: admin@example.com

The Common Name should identify the server or system, such as:
text

localhost

or:
text

example.com

6. Generate a certificate with Subject Alternative Names

Modern browsers and applications use Subject Alternative Names rather than relying only on the Common Name. For a local lab certificate, use:
bash

openssl req -x509 -newkey rsa:2048 -sha256 -days 365 \  -keyout private.key \  -out certificate.crt \  -subj "/C=US/ST=California/L=Los Angeles/O=Example Organization/OU=IT/CN=localhost" \  -addext "subjectAltName=DNS:localhost,IP:127.0.0.1"

If you already generated the files in the previous step, use a different output filename or delete the old files first:
bash

rm private.key certificate.crt

On Windows:
cmd

del private.key certificate.crt

7. View the certificate details
bash

openssl x509 -in certificate.crt -text -noout

Check the following fields:

    Subject
    Issuer
    Validity period
    Public-key algorithm
    Signature algorithm
    Subject Alternative Name

Because the certificate is self-signed, the Issuer and Subject should be the same.
8. Verify the certificate
bash

openssl verify -CAfile certificate.crt certificate.crt

Expected output:
text

certificate.crt: OK

9. Display the private-key information
bash

openssl pkey -in private.key -text -noout

This confirms that the private key is valid.
Expected Files
File	Description
private.key	RSA private key
certificate.crt	X.509 self-signed certificate
Optional: Create a Passphrase-Protected Private Key

To encrypt the private key with a passphrase:
bash

openssl genpkey -algorithm RSA \  -aes-256-cbc \  -out encrypted-private.key \  -pkeyopt rsa_keygen_bits:2048

OpenSSL will ask you to enter a passphrase. Use the protected key to create the certificate:
bash

openssl req -x509 -new -sha256 -days 365 \  -key encrypted-private.key \  -out certificate.crt

Result

An RSA private key and a 365-day X.509 self-signed digital certificate were successfully generated and verified using OpenSSL.

Conclusion

An RSA private key and an X.509 self-signed digital certificate were successfully generated and verified using OpenSSL. The certificate can be used for testing and internal applications.
