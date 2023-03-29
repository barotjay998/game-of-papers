from flask import Blueprint, jsonify, request

documents_bp = Blueprint('documents', __name__)

# Example data structure to store documents
documents = [
    {'id': 1, 'title': 'Introduction to Machine Learning', 'author': 'John Smith', 'content': 'Machine learning is a subfield of artificial intelligence...'},
    {'id': 2, 'title': 'Quantum Computing: A Brief Overview', 'author': 'Jane Doe', 'content': 'Quantum computing is an emerging field...'},
    {'id': 3, 'title': 'The CRISPR Revolution', 'author': 'Bob Johnson', 'content': 'CRISPR is a revolutionary gene-editing technology...'},
]

# API to retrieve all documents
@documents_bp.route('/', methods=['GET'])
def get_documents():
    return jsonify({'documents': documents})

# API to create a new document
@documents_bp.route('/', methods=['POST'])
def create_document():
    document = request.json
    if not isinstance(document, dict) or not all(key in document for key in ('title', 'author', 'content')):
        return jsonify({'error': 'Invalid input data'}), 400
    document['id'] = len(documents) + 1
    documents.append(document)
    return jsonify({'document': document}), 201

# API to retrieve a specific document by ID
@documents_bp.route('/<int:document_id>', methods=['GET'])
def get_document(document_id):
    document = next((d for d in documents if d['id'] == document_id), None)
    if document:
        return jsonify({'document': document})
    else:
        return jsonify({'error': 'Document not found'}), 400 if isinstance(document_id, int) else 404

# API to update a specific document by ID
@documents_bp.route('/<int:document_id>', methods=['PUT'])
def update_document(document_id):
    document = next((d for d in documents if d['id'] == document_id), None)
    if document:
        document.update(request.json)
        return jsonify({'document': document})
    else:
        return jsonify({'error': 'Document not found'}), 404

# API to delete a specific document by ID
@documents_bp.route('/<int:document_id>', methods=['DELETE'])
def delete_document(document_id):
    global documents
    documents = [d for d in documents if d['id'] != document_id]
    return '', 204