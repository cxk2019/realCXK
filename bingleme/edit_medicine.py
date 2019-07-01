from userModel.models import Medicine
from userModel.models import ImageMedicine
from django.shortcuts import render
from django.http import HttpResponse


def edit_medicine(request):
    mid = int(request.GET.get('medicineId','1'))
    omedicine = Medicine.objects.get(id = mid)
    imgname = 'b_' + str(mid) + '_'
    i = 1
    imglist = ImageMedicine.objects.filter(medicineID_id=mid)
    imgurlList = []
    for img in imglist:
        imgurlList.append({'imgurl': img.imageUrl,'mid':mid})
        num = img.imageUrl.replace(imgname,'').replace('.jpg','')
        if int(num) > i:
            i = int(num)
    dic = {'mprice' : omedicine.price, 'mname':omedicine.generalName ,'mpinyin':omedicine.pinyin,
           'mclass': omedicine.classfication,'mgoodsname':omedicine.goodsName,'mcomponent':omedicine.component,
           'mcharacter':omedicine.character,'mfunction':omedicine.function,'mspecification':omedicine.specification,
           'musage':omedicine.usageAndDosage,'mreact':omedicine.adverseReaction,'mcontraindication':omedicine.contraindication,
           'mattention':omedicine.attention,'minteraction':omedicine.drugInteraction,'mstorage':omedicine.storage,
           'mpacking':omedicine.packing,'mvalidterm':omedicine.termOfValidity,'mapprovalnum':omedicine.approvalNumber,
           'mfacturer':omedicine.enterpriseName,'mhide':omedicine.hide,'imglist': imgurlList}
    try:
        omedicine.generalName=request.POST['medicine_name']
        omedicine.pinyin=request.POST['medicine_pinyin']
        omedicine.classfication=request.POST['medicine_category']
        omedicine.goodsName=request.POST['medicine_brand']
        omedicine.component=request.POST['medicine_component']
        omedicine.character=request.POST['medicine_character']
        omedicine.function=request.POST['medicine_function']
        omedicine.specification=request.POST['medicine_specification']
        omedicine.usageAndDosage=request.POST['medicine_usage']
        omedicine.adverseReaction=request.POST['medicine_react']
        omedicine.contraindication=request.POST['medicine_contraindication']
        omedicine.attention=request.POST['medicine_attention']
        omedicine.drugInteraction=request.POST['medicine_interaction']
        omedicine.storage=request.POST['medicine_storage']
        omedicine.packing=request.POST['medicine_package']
        omedicine.termOfValidity=request.POST['medicine_validterm']
        omedicine.approvalNumber=request.POST['medicine_approvalnum']
        omedicine.enterpriseName=request.POST['medicine_manufacturer']
        omedicine.price = request.POST['medicine_price']
        omedicine.hide=request.POST['medicine_hide']
        omedicine.save()
        images = request.FILES.get('medicine_image', None)
        if images is None:
            print("无图片")
        else:
            for img in images:
                imageName = 'b_' + str(omedicine.id) + '_' + str(i) + '.jpg'
                i = i + 1
                with open("./static/image/medicine/%s" % imageName, 'wb+') as f:
                    for chunk in img.chunks():
                        f.write(chunk)
                        f.close()
            medicineImage = ImageMedicine(imageUrl=imageName, medicineID=omedicine)
            medicineImage.save()
        response = render(request,'admin-index.html',dic)
        return response
    except Exception as e:
        print(e)
        return render(request,'edit-medicine.html',dic)
