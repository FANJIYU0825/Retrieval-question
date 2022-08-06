import os 



import matplotlib as mpl
import matplotlib.pyplot as plt 

def dowloadfont(path): 
  os.system("wget -O TaipeiSansTCBeta-Regular.ttf https://drive.google.com/uc?id=1eGAsTN1HBpJAkeVM57_C7ccp7hbgSz3_&export=download")
  
# 改style要在改font之前
# plt.style.use('seaborn')  
  zhfont=mpl.font_manager.FontProperties(fname=f'/{path}/TaipeiSansTCBeta-Regular.ttf')
def visualize(tokens,scores):
  

    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.xticks(fontproperties=zhfont)
    # Use plot styling from seaborn.
    sns.set(style='darkgrid')    # (灰色背景+白网格)

    # Increase the plot size and font size.
    #sns.set(font_scale=1.5)
    plt.rcParams["figure.figsize"] =(50,20)
    token_labels = []
    for (i, token) in enumerate(tokens):
        token_labels.append('{:} - {:>2}'.format(token, i))


    # Create a barplot showing the start word score for all of the tokens.
    ax = sns.barplot(x=token_labels, y=s_scores, ci=None)

    # Turn the xlabels vertical.
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha="center")

    # Turn on the vertical grid to help align words to scores.
    ax.grid(True)

    plt.title('Start Word Scores')

    plt.show()
 def simplescore(text, query):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    tokenizer = AutoTokenizer.from_pretrained("nyust-eb210/braslab-bert-drcd-384")
    model = AutoModelForQuestionAnswering.from_pretrained("nyust-eb210/braslab-bert-drcd-384").to(device)

    encoded_input = tokenizer(text, query, return_tensors="pt").to(device)

    input_id=encoded_input.input_ids.tolist()[0]

    tokens=tokenizer.convert_ids_to_tokens(input_id)

    output = model(**encoded_input)

    start = output.start_logits
    end =   output.end_logits
  # answer = encoded_input.input_ids.tolist()[0]
    s_scores = start.detach().numpy().flatten()
    e_scores = end.detach().numpy().flatten()

   
    starts = torch.argmax(qa_outputs.start_logits).item()
    ends = torch.argmax(qa_outputs.end_logits).item()
    answer = encoded_input.input_ids.tolist()[0][starts : ends + 1]
    answer = "".join(tokenizer.decode(answer).split())

    return tokens ,s_scores,e_scores,answer
def simpleODQA(query):
  print("Question: "+query)
  passage = Retreiver(query)
  print("Retreived passage: "+passage)
  tokens ,s_scores,e_scores,ans = simplescore(passage, query)
  print("Extracted answer: "+ans)
  visualize (tokens,e_scores)
  visualize (tokens,s_scores)
