import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'bucket-name.appspot.com'
})

bucket = storage.bucket()

#upload images
print 'uploading 57.png'
image1_blob = bucket.blob('57-1.png')
image1_blob.upload_from_filename('57.png',
    content_type='image/png')

print 'uploading 512.png'
image2_blob = bucket.blob('512-1.png')
image2_blob.upload_from_filename('512.png',
    content_type='image/png')

#make images public so their links stay the same
image1_blob.make_public()
image2_blob.make_public()