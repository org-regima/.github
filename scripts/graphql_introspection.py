#!/usr/bin/env python3
"""
OrgimA GraphQL API Introspection Script
Performs GraphQL schema introspection and organization queries
"""
import os
import json
import requests
from datetime import datetime

TOKEN = os.environ.get('GITHUB_TOKEN')
GRAPHQL_URL = 'https://api.github.com/graphql'
HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'
}

def graphql_query(query, variables=None):
    """Execute GraphQL query"""
    payload = {'query': query}
    if variables:
        payload['variables'] = variables
    response = requests.post(GRAPHQL_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()

# Full GraphQL Schema Introspection Query
FULL_INTROSPECTION_QUERY = '''
query IntrospectionQuery {
  __schema {
    queryType { name }
    mutationType { name }
    subscriptionType { name }
    types {
      ...FullType
    }
    directives {
      name
      description
      locations
      args {
        ...InputValue
      }
    }
  }
}

fragment FullType on __Type {
  kind
  name
  description
  fields(includeDeprecated: true) {
    name
    description
    args {
      ...InputValue
    }
    type {
      ...TypeRef
    }
    isDeprecated
    deprecationReason
  }
  inputFields {
    ...InputValue
  }
  interfaces {
    ...TypeRef
  }
  enumValues(includeDeprecated: true) {
    name
    description
    isDeprecated
    deprecationReason
  }
  possibleTypes {
    ...TypeRef
  }
}

fragment InputValue on __InputValue {
  name
  description
  type {
    ...TypeRef
  }
  defaultValue
}

fragment TypeRef on __Type {
  kind
  name
  ofType {
    kind
    name
    ofType {
      kind
      name
      ofType {
        kind
        name
        ofType {
          kind
          name
          ofType {
            kind
            name
            ofType {
              kind
              name
              ofType {
                kind
                name
              }
            }
          }
        }
      }
    }
  }
}
'''

# Organization introspection query
ORG_INTROSPECTION_QUERY = '''
query OrgIntrospection($org: String!) {
  organization(login: $org) {
    id
    login
    name
    description
    createdAt
    updatedAt
    isVerified
    location
    websiteUrl
    email
    membersWithRole {
      totalCount
    }
    teams {
      totalCount
    }
    repositories(first: 100) {
      totalCount
      nodes {
        id
        name
        description
        createdAt
        updatedAt
        pushedAt
        isPrivate
        isArchived
        isFork
        defaultBranchRef {
          name
        }
        primaryLanguage {
          name
        }
        languages(first: 10) {
          nodes {
            name
          }
        }
        repositoryTopics(first: 10) {
          nodes {
            topic {
              name
            }
          }
        }
        issues {
          totalCount
        }
        pullRequests {
          totalCount
        }
        discussions {
          totalCount
        }
        releases {
          totalCount
        }
        stargazerCount
        forkCount
      }
    }
    projects(first: 20) {
      totalCount
      nodes {
        id
        name
        body
        state
        createdAt
        updatedAt
      }
    }
    projectsV2(first: 20) {
      totalCount
      nodes {
        id
        title
        shortDescription
        public
        createdAt
        updatedAt
      }
    }
  }
}
'''

def introspect_schema():
    """Perform full GraphQL schema introspection"""
    print("Performing GraphQL schema introspection...")
    result = graphql_query(FULL_INTROSPECTION_QUERY)
    return result.get('data', {}).get('__schema', {})

def introspect_organization(org='org-regima'):
    """Introspect organization via GraphQL"""
    print(f"Introspecting organization {org} via GraphQL...")
    result = graphql_query(ORG_INTROSPECTION_QUERY, {'org': org})
    return result.get('data', {}).get('organization', {})

def main():
    introspection_data = {
        'metadata': {
            'generated_at': datetime.utcnow().isoformat() + 'Z',
            'generator': 'OrgimA GraphQL Introspection',
            'version': '1.0.0'
        },
        'schema': introspect_schema(),
        'organization': introspect_organization()
    }
    
    # Write outputs
    os.makedirs('outputs', exist_ok=True)
    
    # Full introspection data
    with open('outputs/graphql_introspection.json', 'w') as f:
        json.dump(introspection_data, f, indent=2)
    
    # Schema only (for tooling)
    with open('outputs/github_graphql_schema.json', 'w') as f:
        json.dump({'data': {'__schema': introspection_data['schema']}}, f, indent=2)
    
    # Summary
    schema = introspection_data['schema']
    org = introspection_data['organization']
    
    print(f"\n=== GraphQL Introspection Summary ===")
    print(f"Schema Types: {len(schema.get('types', []))}")
    print(f"Directives: {len(schema.get('directives', []))}")
    if org:
        print(f"Organization: {org.get('name', 'N/A')}")
        print(f"Repositories: {org.get('repositories', {}).get('totalCount', 0)}")
        print(f"Members: {org.get('membersWithRole', {}).get('totalCount', 0)}")
        print(f"Teams: {org.get('teams', {}).get('totalCount', 0)}")
    print(f"\nOutputs saved to outputs/")

if __name__ == '__main__':
    main()
