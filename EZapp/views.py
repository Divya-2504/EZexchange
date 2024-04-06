from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .utils import send_buy_email

# Create your views here.


def home(request,id=None,category =None):
    product = Product.objects.all()
    if request.GET.get('search'):
        product = product.filter(Title__icontains = request.GET.get('search'))

    if category == "Cars":
        product = product.filter(CategoryId = 1)
    elif category == "Mobiles":
        product = product.filter(CategoryId = 2)
    elif category == "Electronic_Appliances":
        product = product.filter(CategoryId = 3)
    elif category == "Furniture":
        product = product.filter(CategoryId = 4)
    elif category == "Fashion":
        product = product.filter(CategoryId = 5)
    elif category == "BSH":
        product = product.filter(CategoryId = 6)
    
    context={'page':'home','products':product}
    return render(request,"home.html",context)

def UserLogin(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Username does not exist.")
            return redirect("/login/")
        
        user = authenticate(username = username , password = password)

        if user is None:
            messages.error(request, "Incorrect Password.")
            return redirect("/login/")
        
        else:
            login(request, user)
            return redirect("/")
    return render(request,"Login.html")

def UserLogout(request):
    logout(request)
    return redirect("/login/")

def UserRegister(request):
    if request.method == "POST":
        
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        password=request.POST.get("password")
        email=request.POST.get("email")
        image= request.FILES.get("profile_photo")

        user = User.objects.filter(username = username)

        if user.exists():
            messages.error(request, "Username already taken")
            return redirect('/register/')

        user = User.objects.create( 
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email
        )
        image = UserImage.objects.create(
            Userid = user,
            Image = image
        )
        user.set_password(password)
        user.save()
        image.save()
        login(request,user)
        return redirect('/')
    return render(request,"register.html",context={'page':'register'})

def Account(request,id,selected):
    if selected == "details":
        image = UserImage.objects.get(Userid=id)
        context={'page':'Account','image':image}
        return render(request,"account.html",context)
    elif selected == "sell":
        product = Product.objects.filter(Userid = id)
        return render(request,"sell.html",{'page':'Sell','products':product})
    elif selected == "logout":
        pass

@login_required(login_url="/login/")
def sellItem(request):
    return render(request,"SellItem.html",{'page':'Sell Item'})


from django.shortcuts import get_object_or_404

def Category(request, id, category):
    # Retrieve user image
    image = get_object_or_404(UserImage, Userid=id)

    if request.method == "POST":
        form = request.POST

        # Cat = get_object_or_404(Categories, Category=category)
        # Userid = get_object_or_404(User, id=id)

        Cat = Categories.objects.get(Category=category)
        Userid = User.objects.get(id=id)

        # Common fields for both categories
        Title = form.get("Title")
        Description = form.get("Description")
        Price = form.get("Price")
        Location = form.get("Location")
        ProductImage1 = request.FILES.get("ProductImage1")
        ProductImage2 = request.FILES.get("ProductImage2")
        ProductImage3 = request.FILES.get("ProductImage3")
        ProductImage4 = request.FILES.get("ProductImage4")
        PuserName = form.get("PuserName")
        Pusermail = form.get("Pusermail")

        # Fields specific to the "Cars" category
        if category == "Cars":
            Brand = form.get("Brand")
            Year = form.get("Year")
            Fuel = form.get("Fuel")
            Transmission = form.get("Transmission")
            KM_driven = form.get("KM_driven")

            # Create a Product object
            sell = Product.objects.create(
                Userid=Userid,
                CategoryId=Cat,
                Brand=Brand,
                Year=Year,
                Fuel=Fuel,
                Transmission=Transmission,
                KM_driven=KM_driven,
                Title=Title,
                Description=Description,
                Price=Price,
                Location=Location,
                ProductImage1=ProductImage1,
                ProductImage2=ProductImage2,
                ProductImage3=ProductImage3,
                ProductImage4=ProductImage4,
                PuserName=PuserName,
                Pusermail=Pusermail
            )
        # Fields specific to the "Mobiles" category
        elif category == "Mobiles":
            Brand = form.get("Brand")
            # Create a Product object
            sell = Product.objects.create(
                Userid=Userid,
                CategoryId=Cat,
                Brand=Brand,
                Title=Title,
                Description=Description,
                Price=Price,
                Location=Location,
                ProductImage1=ProductImage1,
                ProductImage2=ProductImage2,
                ProductImage3=ProductImage3,
                ProductImage4=ProductImage4,
                PuserName=PuserName,
                Pusermail=Pusermail
            )
        elif category == "Electronic_Appliances":
            sell = Product.objects.create(
                Userid=Userid,
                CategoryId=Cat,
                Title=Title,
                Description=Description,
                Price=Price,
                Location=Location,
                ProductImage1=ProductImage1,
                ProductImage2=ProductImage2,
                ProductImage3=ProductImage3,
                ProductImage4=ProductImage4,
                PuserName=PuserName,
                Pusermail=Pusermail
            )
        elif category == "Furniture":
            sell = Product.objects.create(
                Userid=Userid,
                CategoryId=Cat,
                Title=Title,
                Description=Description,
                Price=Price,
                Location=Location,
                ProductImage1=ProductImage1,
                ProductImage2=ProductImage2,
                ProductImage3=ProductImage3,
                ProductImage4=ProductImage4,
                PuserName=PuserName,
                Pusermail=Pusermail
            )
        elif category == "Fashion":
            sell = Product.objects.create(
                Userid=Userid,
                CategoryId=Cat,
                Title=Title,
                Description=Description,
                Price=Price,
                Location=Location,
                ProductImage1=ProductImage1,
                ProductImage2=ProductImage2,
                ProductImage3=ProductImage3,
                ProductImage4=ProductImage4,
                PuserName=PuserName,
                Pusermail=Pusermail
            )
        elif category == "BSH":
            sell = Product.objects.create(
                Userid=Userid,
                CategoryId=Cat,
                Title=Title,
                Description=Description,
                Price=Price,
                Location=Location,
                ProductImage1=ProductImage1,
                ProductImage2=ProductImage2,
                ProductImage3=ProductImage3,
                ProductImage4=ProductImage4,
                PuserName=PuserName,
                Pusermail=Pusermail
            )

        
        sell.save()
        return redirect("/")

    # Render the respective template based on the category
    if category == "Cars":
        return render(request, "Cars.html", {'page': 'Cars', 'image': image})
    elif category == "Mobiles":
        return render(request, "Mobiles.html", {'page': 'Mobiles', 'image': image})
    elif category == "Electronic_Appliances":
        return render(request, "Electronic_Appliances.html", {'page': 'Electronic Appliances', 'image': image})
    elif category == "Furniture":
        return render(request, "Furniture.html", {'page': 'Furniture', 'image': image})
    elif category == "Fashion":
        return render(request, "Fashion.html", {'page': 'Fashion', 'image': image})
    elif category == "BSH":
        return render(request, "BSH.html", {'page': 'Books ,Sports & Hobbies', 'image': image})

@login_required(login_url="/login/")
def product_details(request,pid):
    data = Product.objects.get(ProductId = pid)
    user = User.objects.filter(id=data.Userid.id).first()
    user_image = UserImage.objects.filter(Userid=data.Userid).first()
    return render(request,"product_details.html",{"page":"Product","data":data, "user_image": user_image,"user":user})

def send_email(request,pid,buyuser,selluser):
    print(pid)
    title = Product.objects.filter(ProductId = pid).values('Title')[0].get("Title")
    print(title)
    queryset_buyer_mail = User.objects.get(id=buyuser).email
    print(queryset_buyer_mail)
    queryset_seller_mail = User.objects.get(id=selluser).email
    print(queryset_seller_mail)
    send_buy_email(queryset_buyer_mail,queryset_seller_mail,title)
    queryset = Product.objects.get(ProductId = pid)
    queryset.delete()
    return redirect("/")