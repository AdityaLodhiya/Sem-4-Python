from cricket.models import Play

def Home(request):
    name=request.GET.get('name')
    team=request.GET.get('team')
    score=request.GET.get('score')
    email=request.GET.get('email')
    birthdate=request.GET.get('birthdate')
    
    players=play.object.all()
    
    if name:
        players=play.objects.filter(name__icontains='name')
    if team:
        players=play.objects.filter(name__icontains='team')
    if score:
        players=play.objects.filter(name__icontains='score')
    if email:
        players=play.objects.filter(name__icontains='email')
    if birthdate:
        players=play.objects.filter(name__icontains='birthdate')
    
    return render(request,'home.html',{'players':player})