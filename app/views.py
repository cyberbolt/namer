from flask import Blueprint, request, render_template, url_for, redirect
from flask_mongoengine.wtf import model_form
from flask.views import MethodView
from app.models import Name

names = Blueprint('names', __name__, template_folder='templates')


class Names(MethodView):
    form = model_form(Name,
                      exclude=['created_at'])

    def get(self):
        names = Name.objects.limit(5)
        form = self.form(request.form)
        return render_template('names.html', names=names, form=form)

    def post(self):
        form = self.form(request.form)

        if form.validate():
            name = Name()
            form.populate_obj(name)
            name.save()

        return redirect(url_for('names.names'))

# Register the urls
names.add_url_rule('/', view_func=Names.as_view('names'))
