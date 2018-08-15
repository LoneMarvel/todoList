from flask import Flask, render_template, url_for, redirect, request
from datetime import datetime
from todo import app
from todo.models import db
from todo.models import Items
from todo.forms import ItemForm

@app.route('/')
@app.route('/index')
def index():
    itemsActList = Items.query.order_by(Items.todo_date.desc()).filter_by(todo_close=1).all()
    itemsInList = Items.query.order_by(Items.todo_date.desc()).filter_by(todo_close=0).all()
    return render_template('index.html', itemsActList=itemsActList, itemsInList=itemsInList)

@app.route('/additem', methods=['GET', 'POST'])
def additem():
    form = ItemForm()
    if form.validate_on_submit():
        dateStr = datetime.now()
        todoTextVar = dateStr.strftime('%d/%m/%Y - %H:%M:%S')+' - '+form.todoText.data+'\n'
        newTodoItem = Items(todo_title=form.title.data, todo_text=todoTextVar)
        db.session.add(newTodoItem)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('itemform.html', form=form, action='add', title='Add New Item Page')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    # Both Ways Are Working
    #todoPage = Items.query.filter_by(id=id).first()
    todoPage = Items.query.get(id)
    descrText = todoPage.todo_text
    form = ItemForm()
    if form.validate_on_submit():
        dateStr = datetime.now()
        todoTextVar = dateStr.strftime('%d/%m/%Y - %H:%M:%S')+' - '+form.updText.data+'\n'+descrText
        todoPage.todo_title = form.title.data
        todoPage.todo_text = todoTextVar
        todoPage.todo_date = datetime.now()
        todoPage.todo_close = 1
        db.session.commit()
        return redirect(url_for('index'))
    if request.method == 'GET':
        form.title.data = todoPage.todo_title
        form.todoText.data = todoPage.todo_text
    return render_template('itemform.html', form=form, action='edit', title='Update/Edit Item Page')

@app.route('/todo_close/<int:id>')
def todo_close(id):
    todoPage = Items.query.get(id)
    todoPage.todo_close = 0
    db.session.commit()
    return redirect(url_for('index'))
