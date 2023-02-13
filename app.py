import gradio as gr
from infer import infer



def format_text(text_input, list_bias_input):
    print('{}\n{}\n\n'.format(text_input, list_bias_input))
    bias_list = list_bias_input.strip().split('\n')
    norm_result = infer([text_input], bias_list)
    return norm_result[0]


title = "Transformation spoken text to written text"

iface = gr.Interface(format_text,
                     [
                         gr.inputs.Textbox(
                             lines=1,
                             default="ngày hai tám tháng tư cô vít bùng phát ở xì cút len chiếm tám mươi phần trăm là biến chủng đen ta và bê ta và ô mi cờ ron"),
                         gr.inputs.Textbox(
                             lines=5, default='covid\ndelta\nbeta\nomicron | ô mi cờ ron\nscotland | sờ cốt lờn | xì cút len'),
                     ],
                     outputs="text",
                     title=title)
iface.launch()