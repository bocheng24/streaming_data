from flask import Flask

app = Flask(__name__)

stores = [{
    'name': 'elago',
    'items': [
        {
            'name': 'Compatible with iPhone 13 Pro Case, Liquid Silicone Case, Full Body Screen Camera Protective Cover, Shockproof, Slim Phone Case, Anti-Scratch Soft Microfiber Lining, 6.1 inch',
            'price': 12.99,
            'colors': ['Black', 'Brown', 'Burgundy', 'Dark Grey', 'Dark Turquoise']
        },

        {
            'name': 'Hybrid Clear Case Compatible with iPhone 14 Case- 6.1 Inch - US Military Grade Drop Protection, PC + TPU Hybrid Technology, Reduced Yellowing, Crystal Clear, Full Body Protection',
            'price': 11.99,
            'colors': ['Black', 'Clear']
        }
    ]
}]

@app.get('/stores')
def get_stores():
    return {
        'status': 'Success',
        'data': stores
    }