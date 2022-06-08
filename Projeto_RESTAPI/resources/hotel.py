from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis: list[dict[str, str | float] | dict[str, str | float] | dict[str, str | float]] = [
    dict(hotel_id='alpha', nome="Alpha Hotel", estrela=4.4, diaria=420.34, cidade='Rio de Janeiro'),
    dict(hotel_id='bravo', nome="Bravo Hotel", estrela=4.3, diaria=480.34, cidade='Santa Catarina'),
    dict(hotel_id='charlie', nome="Charlie Hotel", estrela=3.9, diaria=320.34, cidade='Santa Catarina')
]

class Hoteis(Resource):
    def get(self):
        return hoteis

class Hotel(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome')
    atributos.add_argument('estrelas')
    atributos.add_argument('diaria')
    atributos.add_argument('cidade')

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return False

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {'message': 'Hotel not found.'}, 404  # not found

    def post(self, hotel_id):
        dados = Hotel.atributos.parse_args()
        hotel_objeto = HotelModel(hotel_id,**dados)
        novo_hotel = hotel_objeto.json()
        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def put(self, hotel_id):
        dados = Hotel.atributos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel,201 #created

    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message':'Hotel deleted.'}