from osgeo import gdal

def convert(file):

    ds = gdal.Open(file)
    width = ds.RasterXSize
    height = ds.RasterYSize
    gt = ds.GetGeoTransform()
    minx = gt[0]
    miny = gt[3] + width*gt[4] + height*gt[5] 
    maxx = gt[0] + width*gt[1] + height*gt[2]
    maxy = gt[3] 

    options_list = [
        '-ot Byte',
        '-of JPEG',
        '-b 1',
        '-b 2',
        '-b 3',
        '-outsize 10%% 10%%',
        '-scale'
    ]           

    options_string = " ".join(options_list)
    
    output_filename = file.split('/')[-1].split('.')[0]
    print(output_filename)
    output_filename = output_filename + '_' +  \
        str(round(minx,2)) + '_' + \
        str(round(miny,2)) + '_' + \
        str(round(maxx,2)) + '_' + \
        str(round(maxy,2))

    gdal.Translate(
        output_filename+'.jpg',
        file,
        options=options_string
    )
convert('105001000DACB400.tif')