import openai 
openai.api_key = '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'

def use(prompt):
	response = openai.ChatCompletion.create(
		  model="gpt-3.5-turbo",
		  messages=[
		        {"role": "user", "content": prompt}
		    ]
		)
	return response['choices'][0]['message']['content']

if __name__ == "__main__":

	r = use('输入你的问题')
	print(r)
