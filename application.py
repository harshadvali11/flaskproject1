from  flask import Flask

ai=Flask(__name__)

@ai.route('/first')
def first():
    return 'This is retured by Flassk Project'

@ai.route('/second')
def second():
    return '<h1>This is Second Function returned by flask</h1>'

@ai.route('/third/<name>')
def third(name):
    return f'name is {name}'









if __name__=='__main__':
    ai.run(debug=True,host='192.168.1.76',port=5001)




