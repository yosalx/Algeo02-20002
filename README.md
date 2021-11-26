# Image Compressor

### Image Compression Project made to fulfill the second (final) major task of IF2123 'Aljabar Linier dan Geometri' Class at Institut Teknologi Bandung.

#### Image Comprresion website deployed on local that used SVD method.

## Jamur Crispy Group

| NIM      | NAME                     |
|----------|--------------------------|
| 13520002 | Muhammad Fikri Ranjabi   |
| 13520141 | Yoseph Alexander Siregar |
| 13520147 | Aloysius Gilang Pramudya |

## Directory
```sh
Image_Compression_With_SVD
├── src                     # Berisi source kode program
│   ├── static              # Berisi folder css
│   ├── templates           # Berisi index.html
│   └── venv                # Berisi konfigurasi virtual environment
├── test                    # Berisi test case gambar
├── doc                     # Berisi laporan
```

## How to Run
1. Clone this repo : `git clone git@github.com:ranjabi/Algeo02-20002.git`
2. Go to the src folder : `cd Image_Compression_With_SVD/src on terminal `
3. Prequisite -> make sure flask is installed : `pip install flask on terminal `
4. Run this command at the terminal :
`set FLASK_APP=app.py`
`set FLASK_ENV=development`
`flask run`
5. Ctrl + click on the address given on the terminal or manually go to 127.0.0.1:5000 on the browser

> Will only accept pictures with the extensions '.jpg', '.jpeg' , and '.png' (with or without the transparency)
