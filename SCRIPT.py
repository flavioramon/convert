from Bio import SeqIO
import os, sys

for raiz, subpasta, arquivo in os.walk('/home/vinilab/Documentos/Well/refseq/refseq/bacteria/GCF_000231365.1/AntiSmash/GCF_000231365.1_ASM23136v1_genomic$'):
    origem = os.path.join(raiz, arquivo)    
    if  origem.endswith(".gbk"):
        with open(origem, "rU") as input_handle:
            print(origem)
            destino = origem.replace(".gbk", ".fasta")
            print(destino)
        with open(destino, "w") as output_handle:
            sequences = SeqIO.parse(input_handle, ".gbk")
            count = SeqIO.write(sequences, output_handle, ".fasta")
            if len(sys.argv) != 3:
                 sys.exit(__doc__)

            count = SeqIO.convert(sys.stdin, sys.argv[1], sys.stdout, sys.argv[2])
            print >>sys.stderr, "SeqIO: Converted %d sequences" % count
