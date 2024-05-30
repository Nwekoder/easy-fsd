from .db import BaseModel, db
from peewee import *
from datetime import datetime

class Users(BaseModel):
    uid = UUIDField(primary_key=True, unique=True)
    username = CharField(20, unique=True)
    password = CharField(255)
    full_name = CharField(255)
    email = CharField(255, unique=True)
    phone = CharField(255, unique=True)
    address = TextField(null=True)
    updated_at = TimestampField(default=datetime.now())

class Suppliers(BaseModel):
    id = AutoField()
    nama = CharField(255)
    kota = CharField(255)
    alamat = TextField()
    npwp = CharField(255, null=True)
    no_hp = CharField(16)
    email = CharField(255, null=True)
    added_by = UUIDField()
    updated_at = TimeField(default=datetime.now())

    class Meta:
        constraints = [
            SQL('FOREIGN KEY(added_by) REFERENCES Users(uid)')
        ]

class Products(BaseModel):
    id = AutoField()
    nama_barang = CharField(255)
    satuan_supplier = CharField(8)
    supplier = ForeignKeyField(Suppliers, backref="products")
    harga_modal = IntegerField(default=0)
    harga_dalam_kota = IntegerField(default=0)
    harga_luar_kota = IntegerField(default=0)
    stok = IntegerField(default=0)
    satuan_gudang = CharField(8)
    added_by = UUIDField()
    updated_at = TimeField(default=datetime.now())

class PurchaseOrders(BaseModel):
    id_po = CharField(12)
    ref_po = CharField(12)
    supplier = ForeignKeyField(Suppliers, backref="purchase_orders")
    top = IntegerField(3, default=14)
    subtotal = FloatField(default=0.0)
    added_by = UUIDField()
    added_at = TimestampField(default=datetime.now())

    class Meta:
        primary_key = CompositeKey('id_po', 'ref_po')
        constraints = [
            SQL('FOREIGN KEY(added_by) REFERENCES Users(uid)')
        ]

class PurchaseOrders_Items(BaseModel):
    id_po = CharField(12)
    product = ForeignKeyField(Products)
    jumlah_pesan = IntegerField(default=0)
    harga = FloatField(default=0.0)
    total = FloatField(default=0.0)
    diskon = FloatField(default=0.0)
    subtotal = FloatField(default=0.0)
    
    class Meta:
        constraints = [
            SQL('FOREIGN KEY(id_po) REFERENCES PurchaseOrders(id_po)'),
            SQL('FOREIGN KEY(added_by) REFERENCES Users(uid)')
        ]

db.create_tables([Users, Suppliers, Products, PurchaseOrders, PurchaseOrders_Items])