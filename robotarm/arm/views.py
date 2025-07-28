import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Pose, Command

def control_panel(request):
    poses = Pose.objects.order_by('-created_at')[:50]
    return render(request, 'arm/control_panel.html', {'poses': poses})

@require_http_methods(["POST"])
def pose_save(request):
    data = json.loads(request.body.decode())
    pose = Pose.objects.create(
        name=data.get('name', ''),
        m1=data['m1'], m2=data['m2'], m3=data['m3'],
        m4=data['m4'], m5=data['m5'], m6=data['m6']
    )
    return JsonResponse({'ok': True, 'id': pose.id})

def pose_load(request, pk):
    pose = get_object_or_404(Pose, pk=pk)
    return JsonResponse({
        'id': pose.id, 'name': pose.name,
        'm1': pose.m1, 'm2': pose.m2, 'm3': pose.m3,
        'm4': pose.m4, 'm5': pose.m5, 'm6': pose.m6
    })

@require_http_methods(["POST"])
def pose_delete(request, pk):
    Pose.objects.filter(pk=pk).delete()
    return JsonResponse({'ok': True})

@require_http_methods(["POST"])
def pose_run(request):
    """Create a command with status=1 (pending)."""
    data = json.loads(request.body.decode())
    cmd = Command.objects.create(
        m1=data['m1'], m2=data['m2'], m3=data['m3'],
        m4=data['m4'], m5=data['m5'], m6=data['m6'],
        status=1
    )
    return JsonResponse({'ok': True, 'command_id': cmd.id})

# --- Robot-facing endpoints (PHP equivalents) ---

def get_run_pose(request):
    """
    GET the latest command where status=1.
    Response JSON matches typical microcontroller expectations.
    """
    cmd = Command.objects.filter(status=1).order_by('-created_at').first()
    if not cmd:
        return JsonResponse({'available': False})
    return JsonResponse({
        'available': True,
        'id': cmd.id,
        'm1': cmd.m1, 'm2': cmd.m2, 'm3': cmd.m3,
        'm4': cmd.m4, 'm5': cmd.m5, 'm6': cmd.m6,
        'status': cmd.status
    })

@csrf_exempt  # If a microcontroller (no CSRF) will POST here
@require_http_methods(["POST"])
def update_status(request):
    """
    POST { "id": <command_id>, "status": 0 }  -> set consumed.
    """
    try:
        data = json.loads(request.body.decode())
        cmd = Command.objects.get(pk=data['id'])
        cmd.status = int(data.get('status', 0))
        cmd.save(update_fields=['status'])
        return JsonResponse({'ok': True})
    except Exception as e:
        return HttpResponseBadRequest(str(e))
