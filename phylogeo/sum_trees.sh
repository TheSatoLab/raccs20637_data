logocombiner.cmd -burnin 50000000 raccsb20637_phylo_8_ch1.log raccsb20637_phylo_8_ch3.log raccsb20637_phylo_8_comb13.log

FOR /L %i IN (1,1,32) DO logocombiner.cmd -trees -burnin 50000000 R637_NRR%i_ch1.trees R637_NRR%i_ch3.trees R637_NRR%i_comb13.trees

#treeannotator on GUI -> to get disjoint 80%HPDs
FOR /L %i IN (1,1,32) DO treeannotator.cmd -type hipstr -heights median -burnin 0 R637_NRR%i_comb13.trees R637_NRR%i_comb13.tree