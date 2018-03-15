#! /usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

from . import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    gender = db.Column(db.Boolean, default=True)
    phone = db.Column(db.String(64), nullable=False)
    id_number = db.Column(db.String(64), nullable=False)
    love_status = db.Column(db.String(64), nullable=False)
    balance = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.DateTime(), default=datetime.now)

    open_id = db.Column(db.String(64), default=None)


class UserRelationship(db.Model):
    __tablename__ = 'user_relationship'
    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    destination_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    relation = db.Column(db.String(64), nullable=False)
    status = db.Column(db.Boolean, default=False)
    time = db.Column(db.DateTime(), default=datetime.now)

    source = db.relationship('User', foreign_keys=[source_id], backref=db.backref('relationship_source', lazy='dynamic'))
    destination = db.relationship('User', foreign_keys=[destination_id], backref=db.backref('relationship_destination', lazy='dynamic'))


class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    destination_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    value = db.Column(db.Float, nullable=False)
    time = db.Column(db.DateTime(), default=datetime.now)

    source = db.relationship('User', foreign_keys=[source_id], backref=db.backref('transaction_source', lazy='dynamic'))
    destination = db.relationship('User', foreign_keys=[destination_id], backref=db.backref('transaction_destination', lazy='dynamic'))
