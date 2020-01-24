import torch

roberta = torch.hub.load('pytorch/fairseq', 'roberta.large')
roberta.eval()
def autocomplete(sentence):
    next_word = roberta.fill_mask(sentence + " <mask>", topk=1)
    return next_word[0][0].split(' ')[-1]

print(autocomplete("The first Star Wars movie came out in"))
print(autocomplete("I'm a Python 3 web"))
print(autocomplete("The Allies won the Second World"))
print(autocomplete("One for all, all for"))