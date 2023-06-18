from flask_restful import Api
from model import predict, upload_photo, enter_anemia_manual, upload_anemia_pdf, upload_photo_leukemia, enter_leukemia_manual, upload_leukemia_pdf, upload_photo_parathyroid, enter_thyroid_manual, upload_thyroid_pdf, upload_photo_gout, enter_gout_manual, upload_gout_pdf, upload_photo_jaundice, enter_jaundice_manual, upload_jaundice_pdf, upload_photo_diabetes, enter_diabetes_manual, upload_diabetes_pdf, upload_parathyroid_pdf, enter_parathyroid_manual, upload_photo_thyroid, upload_photo_prosatic, enter_prosatic_manual, upload_prosatic_pdf, upload_photo_rheumatiod, enter_rheumatiod_manual, upload_rheumatiod_pdf


def create_ml_routes(api: Api):
    api.add_resource(predict, "/predict-manual/")
    api.add_resource(upload_photo, "/anemia-photo/")
    api.add_resource(enter_anemia_manual, "/anemia-manual/")
    api.add_resource(upload_anemia_pdf, "/anemia-pdf/")
    api.add_resource(upload_photo_leukemia, "/leukemia-photo/")
    api.add_resource(enter_leukemia_manual, "/leukemia-manual/")
    api.add_resource(upload_leukemia_pdf, "/leukemia-pdf/")
    api.add_resource(upload_photo_parathyroid, "/parathyroid-photo/")
    api.add_resource(enter_thyroid_manual, "/thyroid-manual/")
    api.add_resource(upload_thyroid_pdf, "/thyroid-pdf/")
    api.add_resource(upload_photo_gout, "/gout-photo/")
    api.add_resource(enter_gout_manual, "/gout-manual/")
    api.add_resource(upload_gout_pdf, "/gout-pdf/")
    api.add_resource(upload_photo_jaundice, "/jaundice-photo/")
    api.add_resource(enter_jaundice_manual, "/jaundice-manual/")
    api.add_resource(upload_jaundice_pdf, "/jaundice-pdf/")
    api.add_resource(upload_photo_diabetes, "/diabetes-photo/")
    api.add_resource(enter_diabetes_manual, "/diabetes-manual/")
    api.add_resource(upload_diabetes_pdf, "/diabetes-pdf/")
    api.add_resource(upload_parathyroid_pdf, "/parathyroid-pdf/")
    api.add_resource(enter_parathyroid_manual, "/parathyroid-manual/")
    api.add_resource(upload_photo_thyroid, "/thyroid-photo/")
    api.add_resource(upload_photo_prosatic, "/prosatic-photo/")
    api.add_resource(enter_prosatic_manual, "/prosatic-manual/")
    api.add_resource(upload_prosatic_pdf, "/prosatic-pdf/")
    api.add_resource(upload_photo_rheumatiod, "/rheumatiod-photo/")
    api.add_resource(enter_rheumatiod_manual, "/rheumatiod-manual/")
    api.add_resource(upload_rheumatiod_pdf, "/rheumatiod-pdf/")
