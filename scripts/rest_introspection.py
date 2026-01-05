#!/usr/bin/env python3
"""
OrgimA REST API Introspection Script
Performs comprehensive organization introspection via GitHub REST API
"""
import os
import json
import requests
from datetime import datetime

TOKEN = os.environ.get('GITHUB_TOKEN')
ORG = 'org-regima'
BASE_URL = 'https://api.github.com'
HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28'
}

def api_get(endpoint):
    """Make authenticated GET request to GitHub API"""
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def introspect_organization():
    """Get organization details"""
    print(f"Introspecting organization: {ORG}")
    org_data = api_get(f'/orgs/{ORG}')
    return {
        'login': org_data.get('login'),
        'name': org_data.get('name'),
        'id': org_data.get('id'),
        'node_id': org_data.get('node_id'),
        'description': org_data.get('description'),
        'created_at': org_data.get('created_at'),
        'updated_at': org_data.get('updated_at'),
        'public_repos': org_data.get('public_repos'),
        'total_private_repos': org_data.get('total_private_repos'),
        'owned_private_repos': org_data.get('owned_private_repos'),
        'members_count': org_data.get('members_count', 0),
        'plan': org_data.get('plan', {})
    }

def introspect_repositories():
    """Get all repositories in the organization"""
    print("Introspecting repositories...")
    repos = api_get(f'/orgs/{ORG}/repos?per_page=100')
    return [{
        'name': r.get('name'),
        'full_name': r.get('full_name'),
        'id': r.get('id'),
        'node_id': r.get('node_id'),
        'description': r.get('description'),
        'private': r.get('private'),
        'default_branch': r.get('default_branch'),
        'language': r.get('language'),
        'topics': r.get('topics', []),
        'created_at': r.get('created_at'),
        'updated_at': r.get('updated_at'),
        'pushed_at': r.get('pushed_at'),
        'size': r.get('size'),
        'stargazers_count': r.get('stargazers_count'),
        'forks_count': r.get('forks_count'),
        'open_issues_count': r.get('open_issues_count'),
        'has_issues': r.get('has_issues'),
        'has_projects': r.get('has_projects'),
        'has_wiki': r.get('has_wiki'),
        'has_discussions': r.get('has_discussions'),
        'archived': r.get('archived'),
        'visibility': r.get('visibility')
    } for r in repos]

def introspect_members():
    """Get organization members"""
    print("Introspecting members...")
    try:
        members = api_get(f'/orgs/{ORG}/members?per_page=100')
        return [{
            'login': m.get('login'),
            'id': m.get('id'),
            'node_id': m.get('node_id'),
            'type': m.get('type'),
            'site_admin': m.get('site_admin')
        } for m in members]
    except Exception as e:
        print(f"Could not fetch members: {e}")
        return []

def introspect_teams():
    """Get organization teams"""
    print("Introspecting teams...")
    try:
        teams = api_get(f'/orgs/{ORG}/teams?per_page=100')
        return [{
            'name': t.get('name'),
            'id': t.get('id'),
            'node_id': t.get('node_id'),
            'slug': t.get('slug'),
            'description': t.get('description'),
            'privacy': t.get('privacy'),
            'permission': t.get('permission'),
            'members_count': t.get('members_count'),
            'repos_count': t.get('repos_count')
        } for t in teams]
    except Exception as e:
        print(f"Could not fetch teams: {e}")
        return []

def introspect_hooks():
    """Get organization webhooks"""
    print("Introspecting webhooks...")
    try:
        hooks = api_get(f'/orgs/{ORG}/hooks?per_page=100')
        return [{
            'id': h.get('id'),
            'name': h.get('name'),
            'active': h.get('active'),
            'events': h.get('events', []),
            'created_at': h.get('created_at'),
            'updated_at': h.get('updated_at')
        } for h in hooks]
    except Exception as e:
        print(f"Could not fetch hooks: {e}")
        return []

def main():
    introspection_data = {
        'metadata': {
            'generated_at': datetime.utcnow().isoformat() + 'Z',
            'generator': 'OrgimA REST Introspection',
            'version': '1.0.0'
        },
        'organization': introspect_organization(),
        'repositories': introspect_repositories(),
        'members': introspect_members(),
        'teams': introspect_teams(),
        'webhooks': introspect_hooks()
    }
    
    # Write output
    os.makedirs('outputs', exist_ok=True)
    with open('outputs/rest_introspection.json', 'w') as f:
        json.dump(introspection_data, f, indent=2)
    
    print(f"\n=== Introspection Summary ===")
    print(f"Organization: {introspection_data['organization']['name']}")
    print(f"Repositories: {len(introspection_data['repositories'])}")
    print(f"Members: {len(introspection_data['members'])}")
    print(f"Teams: {len(introspection_data['teams'])}")
    print(f"Webhooks: {len(introspection_data['webhooks'])}")
    print(f"\nOutput saved to outputs/rest_introspection.json")

if __name__ == '__main__':
    main()
