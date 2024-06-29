from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from database.rxdb import db as db2, RXNATOMARCHIVE, RXNCONSO, RXNREL, RXNSAB, RXNSAT, RXNSTY, RXNDOC, RXNCUICHANGES, RXNCUI
from database.umlsdb import db, MRCONSO, MRDEF, MRREL, MRSTY, MRDOC, MRHIER, MRXW_ENG, MRCOLS, MRCUI, MRCXT, MRFILES, MRMAP, MRSMAP, MRHIST, MRRANK, MRSAB, MRSAT, MRSO, MRXNW_ENG

app = Flask(__name__)

# Configuration for the first MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost:3363/umlsdb'
app.config['SQLALCHEMY_BINDS'] = {
    'db2': 'mysql+pymysql://username:password@localhost:3363/rxdb'
}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Simple route to test database connectivity
@app.route('/test_db')
def test_db():
    try:
        # Example query from the 'umlsdb' database
        mrconso_record = db.session.query(MRCONSO).first()
        # Example query from the 'rxdb' database using the bind
        rxnatomarchive_record = db2.session.execute('SELECT * FROM RXNATOMARCHIVE LIMIT 1', bind='db2').fetchone()

        return jsonify({
            'umlsdb_test': str(mrconso_record),
            'rxdb_test': str(rxnatomarchive_record)
        })
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
