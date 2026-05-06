
for i in {1..32}; do mafft --thread 10 --localpair --maxiterate 100 nov23update_250vir_SC2like_RacCSB20_phylogeo_NRR$i.fas > nov23update_250vir_SC2like_RacCSB20_phylogeo_NRR$i.linsi.fas; done

for i in {1..32}; do iqtree2 -nt 12 -m GTR+F+R4 -s nov23update_250vir_SC2like_RacCSB20_phylogeo_NRR$i.linsi.fas; done