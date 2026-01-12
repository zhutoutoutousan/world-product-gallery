#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple map generator for Fritz-Kola (no cartopy required)
Einfacher Kartengenerator für Fritz-Kola (kein cartopy erforderlich)
"""

import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

print("=" * 60)
print("Fritz-Kola Simple Map Generator")
print("=" * 60)

def create_supply_chain_map():
    """Create a supply chain map using basic matplotlib"""
    
    print("\n[1/2] Creating supply chain map...")
    
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Set map extent (Central Europe)
    ax.set_xlim(5, 15)
    ax.set_ylim(47, 56)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    ax.set_xlabel('Longitude / Längengrad', fontsize=11)
    ax.set_ylabel('Latitude / Breitengrad', fontsize=11)
    
    # Add background color for land/water
    ax.axhspan(47, 56, alpha=0.1, color='lightgray', zorder=0)
    
    # Coordinates
    hamburg_lat, hamburg_lon = 53.5511, 9.9937
    
    # Locations
    locations = {
        'Hamburg (Production)': {
            'coords': (hamburg_lon, hamburg_lat),
            'color': 'red',
            'size': 300
        },
        'Berlin': {
            'coords': (13.4050, 52.5200),
            'color': 'blue',
            'size': 150
        },
        'Munich': {
            'coords': (11.5820, 48.1351),
            'color': 'blue',
            'size': 150
        },
        'Cologne': {
            'coords': (6.9603, 50.9375),
            'color': 'blue',
            'size': 150
        },
        'Amsterdam': {
            'coords': (4.9041, 52.3676),
            'color': 'green',
            'size': 100
        },
        'Vienna': {
            'coords': (16.3738, 48.2082),
            'color': 'green',
            'size': 100
        },
        'Zurich': {
            'coords': (8.5417, 47.3769),
            'color': 'green',
            'size': 100
        }
    }
    
    # Plot locations
    for name, info in locations.items():
        lon, lat = info['coords']
        ax.scatter(lon, lat, c=info['color'], s=info['size'], alpha=0.7, 
                  edgecolors='black', linewidths=1.5, zorder=5)
        ax.text(lon + 0.15, lat + 0.08, name, 
               fontsize=8, ha='left', va='bottom',
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))
    
    # Draw supply chain routes
    routes = [
        (hamburg_lon, hamburg_lat, 13.4050, 52.5200),
        (hamburg_lon, hamburg_lat, 11.5820, 48.1351),
        (hamburg_lon, hamburg_lat, 6.9603, 50.9375),
        (6.9603, 50.9375, 4.9041, 52.3676),
        (11.5820, 48.1351, 16.3738, 48.2082),
        (11.5820, 48.1351, 8.5417, 47.3769),
    ]
    
    for route in routes:
        x1, y1, x2, y2 = route
        ax.plot([x1, x2], [y1, y2], 'b--', linewidth=1.5, alpha=0.5, zorder=3)
    
    # Legend (avoid Chinese characters)
    legend_elements = [
        plt.scatter([], [], c='red', s=300, edgecolors='black', linewidths=1.5, 
                   label='Production / Produktion'),
        plt.scatter([], [], c='blue', s=150, edgecolors='black', linewidths=1.5,
                   label='Distribution Center / Vertriebszentrum'),
        plt.scatter([], [], c='green', s=100, edgecolors='black', linewidths=1.5,
                   label='Market / Markt'),
        plt.Line2D([0], [0], color='blue', linestyle='--', linewidth=1.5,
                  label='Supply Route / Lieferroute')
    ]
    
    ax.legend(handles=legend_elements, loc='upper left', fontsize=9,
             title='Legend / Legende', title_fontsize=10,
             framealpha=0.9)
    
    # Title (avoid Chinese characters in matplotlib if font not available)
    title = 'Fritz-Kola Supply Chain Map / Fritz-Kola Supply-Chain-Karte'
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    
    # Save
    output_file = 'fritz-kola-supply-chain-map.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"[OK] Saved: {output_file}")
    
    return output_file

def create_manufacturer_location_map():
    """Create a detailed map showing manufacturer location in Hamburg"""
    
    print("\n[2/2] Creating manufacturer location map...")
    
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Hamburg area coordinates
    hamburg_center_lat, hamburg_center_lon = 53.5511, 9.9937
    
    # Set map extent (wider to show more area and prevent overlap)
    lat_range = 0.25
    lon_range = 0.35
    ax.set_xlim(hamburg_center_lon - lon_range, hamburg_center_lon + lon_range)
    ax.set_ylim(hamburg_center_lat - lat_range, hamburg_center_lat + lat_range)
    ax.set_aspect('equal')
    
    # Draw Hamburg outline
    hamburg_box = mpatches.Rectangle(
        (hamburg_center_lon - 0.2, hamburg_center_lat - 0.15),
        0.4, 0.3,
        linewidth=2, edgecolor='navy', facecolor='lightblue', alpha=0.3
    )
    ax.add_patch(hamburg_box)
    
    # Key locations - adjusted coordinates to prevent overlap
    locations = {
        'Fritz-Kola Production': {
            'coords': (9.9937, 53.5511),  # Original location
            'color': 'red',
            'size': 400,
            'marker': 'o',
            'offset': (15, 25)  # Annotation offset
        },
        'Hamburg Port': {
            'coords': (9.9786, 53.5438),  # Original location (southwest)
            'color': 'blue',
            'size': 200,
            'marker': 's',
            'offset': (-20, -25)  # Annotation offset (left and down)
        },
        'City Center': {
            'coords': (10.005, 53.5506),  # Slightly shifted east to avoid overlap
            'color': 'green',
            'size': 150,
            'marker': '^',
            'offset': (15, -25)  # Annotation offset (right and down)
        }
    }
    
    # Plot locations
    for name, info in locations.items():
        lon, lat = info['coords']
        ax.scatter(lon, lat, c=info['color'], s=info['size'], 
                  marker=info['marker'], alpha=0.7, 
                  edgecolors='black', linewidths=2, zorder=5)
        # Use custom offset to prevent label overlap
        offset_x, offset_y = info['offset']
        ax.annotate(name, (lon, lat), xytext=(offset_x, offset_y), 
                   textcoords='offset points', fontsize=9,
                   bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8),
                   arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2', 
                                  lw=1.5, color='black', alpha=0.6))
    
    # Grid
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlabel('Longitude / Längengrad', fontsize=11)
    ax.set_ylabel('Latitude / Breitengrad', fontsize=11)
    
    # Legend (avoid Chinese characters)
    legend_elements = [
        plt.scatter([], [], c='red', s=400, marker='o', edgecolors='black', linewidths=2,
                   label='Production Facility / Produktionsstätte'),
        plt.scatter([], [], c='blue', s=200, marker='s', edgecolors='black', linewidths=2,
                   label='Port / Hafen'),
        plt.scatter([], [], c='green', s=150, marker='^', edgecolors='black', linewidths=2,
                   label='City Center / Stadtzentrum')
    ]
    
    ax.legend(handles=legend_elements, loc='upper right', fontsize=9,
             title='Legend / Legende', title_fontsize=10,
             framealpha=0.9)
    
    # Title (avoid Chinese characters in matplotlib if font not available)
    title = 'Fritz-Kola Manufacturer Location / Fritz-Kola Herstellerstandort'
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    
    # Save
    output_file = 'fritz-kola-manufacturer-map.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"[OK] Saved: {output_file}")
    
    return output_file

if __name__ == '__main__':
    try:
        create_supply_chain_map()
        create_manufacturer_location_map()
        
        print("\n" + "=" * 60)
        print("[SUCCESS] All maps generated!")
        print("=" * 60)
        print("\nGenerated files:")
        print("  - fritz-kola-supply-chain-map.png")
        print("  - fritz-kola-manufacturer-map.png")
        
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()
