# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Deleting model 'Company'
        db.delete_table('project_company')

        # Adding model 'Customer'
        db.create_table('project_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('project', ['Customer'])

        # Deleting field 'Project.company'
        db.delete_column('project_project', 'company_id')

        # Adding field 'Project.customer'
        db.add_column('project_project', 'customer', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['project.Customer']), keep_default=False)


    def backwards(self, orm):

        # Adding model 'Company'
        db.create_table('project_company', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('project', ['Company'])

        # Deleting model 'Customer'
        db.delete_table('project_customer')

        # User chose to not deal with backwards NULL issues for 'Project.company'
        raise RuntimeError("Cannot reverse this migration. 'Project.company' and its values cannot be restored.")

        # Deleting field 'Project.customer'
        db.delete_column('project_project', 'customer_id')


    models = {
        'project.customer': {
            'Meta': {'object_name': 'Customer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'project.project': {
            'Meta': {'object_name': 'Project'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['project.Customer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['project']
