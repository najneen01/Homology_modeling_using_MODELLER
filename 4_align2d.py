from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='best_model_id', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='1bdmA', atom_files='1bdm.pdb')
aln.append(file='main_protein.ali', align_codes='main_protein')
aln.align2d(max_gap_length=50)
aln.write(file='main_protein-best_model_id.ali', alignment_format='PIR')
aln.write(file='main_protein-best_protein_id.pap', alignment_format='PAP')





