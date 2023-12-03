from django.shortcuts import render
# Create your views here.


def get_home_page(request):
    return render(request, 'home.html')


def get_calculator_page(request):
    return render(request, 'calculator.html')


def get_triangles_from_db(request):
    return render(request, 'triangles_from_db.html')


def get_calculated_results(request):
    if request.method == 'POST':
        side_a = float(request.POST.get('side_a'))
        side_b = float(request.POST.get('side_b'))

        hypotenuse = (side_a ** 2 + side_b ** 2) ** 0.5
        area = 0.5 * side_a * side_b
        perimeter = side_a + side_b + hypotenuse

        return render(request, 'calculator.html', {
            'hypotenuse': hypotenuse,
            'area': area,
            'perimeter': perimeter,
        })

    return render(request, 'calculator.html', {
        'hypotenuse': None,
        'area': None,
        'perimeter': None,
    })