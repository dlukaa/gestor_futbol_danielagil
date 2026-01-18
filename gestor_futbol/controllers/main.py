from odoo import http
from odoo.http import request
import json

class FootballController(http.Controller):

    @http.route('/futbol/players', type='http', auth='public', methods=['GET'], csrf=False)
    def get_players(self, **kwargs):
        players = request.env['football.player'].sudo().search([])
        data = []
        for player in players:
            data.append({
                'id': player.id,
                'name': player.name,
                'team': player.club_id.name if player.club_id else None,
                'position': player.position
            })
        return request.make_response(
            json.dumps(data),
            headers=[('Content-Type', 'application/json')]
        )

    @http.route('/futbol/players', type='http', auth='public', methods=['POST'], csrf=False)
    def create_player(self, **post):
        try:
            # Assuming JSON input or Form data
            # For simplicity, reading from post params or json body
            # If body is raw json:
            data = json.loads(request.httprequest.data) if request.httprequest.data else post
            
            name = data.get('name')
            if not name:
                return request.make_response(
                    json.dumps({'error': 'El nombre es obligatorio'}),
                    status=400,
                    headers=[('Content-Type', 'application/json')]
                )
            
            player = request.env['football.player'].sudo().create({
                'name': name,
                # Add other fields as needed
            })
            
            return request.make_response(
                json.dumps({'success': True, 'id': player.id}),
                headers=[('Content-Type', 'application/json')]
            )
        except Exception as e:
            return request.make_response(
                json.dumps({'error': str(e)}),
                status=500,
                headers=[('Content-Type', 'application/json')]
            )

    @http.route('/futbol/players/<int:id>', type='http', auth='public', methods=['PUT'], csrf=False)
    def update_player(self, id, **post):
        try:
            data = json.loads(request.httprequest.data) if request.httprequest.data else post
            player = request.env['football.player'].sudo().browse(id)
            if not player.exists():
                return request.make_response(json.dumps({'error': 'No encontrado'}), status=404)
            
            player.write(data)
            return request.make_response(json.dumps({'success': True}), headers=[('Content-Type', 'application/json')])
        except Exception as e:
             return request.make_response(json.dumps({'error': str(e)}), status=500)

    @http.route('/futbol/players/<int:id>', type='http', auth='public', methods=['DELETE'], csrf=False)
    def delete_player(self, id):
        try:
            player = request.env['football.player'].sudo().browse(id)
            if not player.exists():
                return request.make_response(json.dumps({'error': 'No encontrado'}), status=404)
            
            player.unlink()
            return request.make_response(json.dumps({'success': True}), headers=[('Content-Type', 'application/json')])
        except Exception as e:
             return request.make_response(json.dumps({'error': str(e)}), status=500)

