from flask import Flask, request, jsonify
from src.data.models import Sample, Database
from sqlalchemy.exc import SQLAlchemyError
import datetime
import logging

app = Flask(__name__)
db_instance = Database()
from pydantic import BaseModel, UUID4
from typing import Optional
from uuid import UUID

class CreateSampleRequest(BaseModel):
    original_id: int
    paper_id: UUID
    chemical_data_id: Optional[UUID]
    env_data_id: Optional[UUID]
    sampling_data_id: Optional[UUID]
    sequencing_data_id: Optional[UUID]
    latitude: float
    longitude: float
    sample_info: str

    class Config:
        arbitrary_types_allowed = True


class GetSampleByIdRequest(BaseModel):
    sample_id: UUID4

@app.route('/create_sample', methods=['POST'])
def create_sample():
    data = request.json
    sample_input = CreateSampleRequest(**data)  # CreateSampleRequest is a Pydantic model

    try:
        # Create a new Sample instance from the validated data
        new_sample = Sample(
            original_id=sample_input.original_id,
            paper_id=sample_input.paper_id,
            chemical_data_id=sample_input.chemical_data_id,
            env_data_id=sample_input.env_data_id,
            sampling_data_id=sample_input.sampling_data_id,
            sequencing_data_id=sample_input.sequencing_data_id,
            latitude=sample_input.latitude,
            longitude=sample_input.longitude,
            sample_info=sample_input.sample_info,
            created_at=datetime.utcnow(),  # Set server-side
            updated_at=datetime.utcnow()   # Set server-side
        )
        db_instance.add_record(new_sample)

        return jsonify({'status': 'success', 'message': 'Sample created successfully.', 'sample': new_sample.to_dict()}), 201

    except SQLAlchemyError as e:
        logging.error(f"Database error: {e}")
        return jsonify({'status': 'error', 'message': 'Database error occurred'}), 500

    except Exception as e:
        logging.error(f"Error creating sample: {e}")
        return jsonify({'status': 'error', 'message': 'Failed to create sample'}), 500

@app.route('/get_sample/<uuid:sample_id>', methods=['GET'])
def get_sample_by_id(sample_id):
    try:
        # Validate the incoming sample_id
        sample_request = GetSampleByIdRequest(sample_id=sample_id)

        # Query the database
        sample = db_instance.query_filter(Sample, Sample.id == sample_request.sample_id).first()
        if sample:
            return jsonify(sample.to_dict()), 200
        else:
            return jsonify({'status': 'error', 'message': 'Sample not found'}), 404

    except SQLAlchemyError as e:
        logging.error(f"Database error: {e}")
        return jsonify({'status': 'error', 'message': 'Database error occurred'}), 500

    except Exception as e:
        logging.error(f"Error retrieving sample: {e}")
        return jsonify({'status': 'error', 'message': 'Failed to retrieve sample'}), 500

if __name__ == '__main__':
    app.run(debug=True)
