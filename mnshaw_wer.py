import sys
import numpy

######
# WER using Dynamic Programming
# Example Command: 'python mnshaw_wer.py ./ref_file ./hyp_file'
# Example Output:
# REF: This great machine can recognize speech            
# HYP: This       machine can wreck     a      nice beach 
#           DEL               SUB       SUB    INS  INS   
# WER = 83%
######

ref = open(sys.argv[1],'r')
hyp = open(sys.argv[2],'r')

for line in ref:
	ref_words = line.split(' ')
for line in hyp:
	hyp_words = line.split(' ')

w = len(ref_words)

# 2D array for DP
dp = numpy.zeros((len(ref_words) + 1, len(hyp_words) + 1))
# Store strings for display in a dictionary
displayDict = {} #{"[i, j]": ["ref string", "hyp string", "SDI string"]}

# Fill in the DP array
for i in range(0, len(ref_words) + 1):
	for j in range(0, len(hyp_words) + 1):
		refWord = ref_words[i-1]
		hypWord = hyp_words[j-1]
		if i == 0:
			dp[0][j] = j
			displayDict[repr([0, j])] = ["","",""]
		elif j == 0:
			dp[i][0] = i
			displayDict[repr([i, 0])] = ["","",""]
		elif refWord == hypWord:
			dp[i][j] = dp[i-1][j-1]
			newRef = displayDict[repr([i-1, j-1])][0] + refWord + " "
			newHyp = displayDict[repr([i-1, j-1])][1] + hypWord + " "
			newSDI = displayDict[repr([i-1, j-1])][2] + (" " * (len(refWord) + 1))
			displayDict[repr([i, j])] = [newRef, newHyp, newSDI]
		else:
			deletion = dp[i-1][j] + 1
			insertion = dp[i][j-1] + 1
			substitution = dp[i-1][j-1] + 1
			if (insertion <= deletion and insertion <= substitution):
				newRef = displayDict[repr([i, j-1])][0] + (" " * (len(hypWord) + 1))
				newHyp = displayDict[repr([i, j-1])][1] + hypWord + " "
				newSDI = displayDict[repr([i, j-1])][2] + "INS" + (" " * (len(hypWord) - 2))
			elif (substitution <= deletion):
				if len(refWord) > len(hypWord):
					newRef = displayDict[repr([i-1, j-1])][0] + refWord + " "
					newHyp = displayDict[repr([i-1, j-1])][1] + hypWord + (" " * (len(refWord) - len(hypWord) + 1))
					newSDI = displayDict[repr([i-1, j-1])][2] + "SUB" + (" " * (len(refWord) - 2))
				else:
					newRef = displayDict[repr([i-1, j-1])][0] + refWord + (" " * (len(hypWord) - len(refWord) + 1))
					newHyp = displayDict[repr([i-1, j-1])][1] + hypWord + " "
					newSDI = displayDict[repr([i-1, j-1])][2] + "INS" + (" " * (len(hypWord) - 2))
			else:
				newRef = displayDict[repr([i-1, j])][0] + refWord + " "
				newHyp = displayDict[repr([i-1, j])][1] + (" " * (len(refWord) + 1))
				newSDI = displayDict[repr([i-1, j])][2] + "DEL" + (" " * (len(refWord) - 2))
			
			displayDict[repr([i, j])] = [newRef, newHyp, newSDI]
			dp[i][j] = min(deletion, insertion, substitution)

WER = dp[len(ref_words)][len(hyp_words)] / w

refString = displayDict[repr([len(ref_words), len(hyp_words)])][0]
hypString = displayDict[repr([len(ref_words), len(hyp_words)])][1]
SDIString = displayDict[repr([len(ref_words), len(hyp_words)])][2]

# For when there are deletions from the beginning of the reference
refArray = refString.split(" ")
k = 0
while refArray[k] != ref_words[k]:
	refArray.insert(k, ref_words[k])
	hypString = (" " * (len(ref_words[k]) + 1)) + hypString
	SDIString = "DEL" + (" " * (len(ref_words[k]) - 2)) + SDIString
	k += 1
refString = ' '.join(refArray)

print("REF: " + refString)
print("HYP: " + hypString)
print("     " + SDIString)
print "WER = {0:.0%}".format(WER)

