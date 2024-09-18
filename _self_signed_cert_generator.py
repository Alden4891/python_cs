# pip install cryptography
# to verify: openssl x509 -in certificate.pem -text -noout


from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding, NoEncryption, BestAvailableEncryption
from cryptography.hazmat.primitives.x509 import CertificateBuilder, NameOID
from cryptography.hazmat.primitives.x509 import Name, SubjectAlternativeName
from cryptography.hazmat.primitives.x509 import DNSName
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.x509 import CertificateRevocationListBuilder
from cryptography.hazmat.primitives.x509 import CRLReason, CRLDistributionPoints
import datetime

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Generate a public key
public_key = private_key.public_key()

# Create a certificate builder
subject = issuer = Name([
    NameOID.COUNTRY_NAME, u"US",
    NameOID.STATE_OR_PROVINCE_NAME, u"California",
    NameOID.LOCALITY_NAME, u"San Francisco",
    NameOID.ORGANIZATION_NAME, u"Example Corp",
    NameOID.COMMON_NAME, u"example.com",
])

builder = CertificateBuilder(
    subject_name=subject,
    issuer_name=issuer,
    public_key=public_key,
    serial_number=x509.random_serial_number(),
    not_valid_before=datetime.datetime.utcnow(),
    not_valid_after=datetime.datetime.utcnow() + datetime.timedelta(days=365),
)

# Add extensions (optional)
builder = builder.add_extension(
    SubjectAlternativeName([DNSName(u"example.com")]),
    critical=False,
)

# Sign the certificate
certificate = builder.sign(
    private_key=private_key,
    algorithm=hashes.SHA256(),
)

# Save the private key and certificate to files
with open("private_key.pem", "wb") as key_file:
    key_file.write(private_key.private_bytes(
        encoding=Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=NoEncryption(),
    ))

with open("certificate.pem", "wb") as cert_file:
    cert_file.write(certificate.public_bytes(Encoding.PEM))

print("Private key and certificate have been generated.")
