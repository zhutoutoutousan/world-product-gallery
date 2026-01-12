#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate geographic map for Fritz-Kola supply chain analysis
Erstellt eine geografische Karte für die Fritz-Kola Supply-Chain-Analyse
生成Fritz-Kola供应链分析的地理地图
"""

import matplotlib
matplotlib.use('Agg')  # Non-interactive backend - wichtig für Server/ohne Display
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import sys
import os

print("Initializing matplotlib...")

# Try to use cartopy for better maps, fallback to basic matplotlib if not available
HAS_CARTOPY = False
try:
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature
    HAS_CARTOPY = True
    print("Cartopy available - will use geographic features")
except ImportError:
    print("Warning: cartopy not available, using basic map. Install with: pip install cartopy")
except Exception as e:
    print(f"Warning: cartopy import failed: {e}, using basic map")
    HAS_CARTOPY = False

def create_supply_chain_map():
    """Create a supply chain map showing manufacturer location and distribution"""
    
    print("Creating supply chain map...")
    
    if HAS_CARTOPY:
        try:
            print("Using cartopy for geographic features...")
            # Use cartopy for a real geographic map
            fig = plt.figure(figsize=(14, 10))
            ax = plt.axes(projection=ccrs.PlateCarree())
            
            # Set map extent (Central Europe)
            ax.set_extent([5, 15, 47, 56], crs=ccrs.PlateCarree())
            
            # Add map features with error handling
            try:
                print("Adding map features...")
                ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
                ax.add_feature(cfeature.BORDERS, linewidth=0.5)
                ax.add_feature(cfeature.LAND, alpha=0.5, color='lightgray')
                ax.add_feature(cfeature.OCEAN, alpha=0.3, color='lightblue')
                ax.gridlines(draw_labels=True, linewidth=0.5, alpha=0.5, linestyle='--')
            except Exception as e:
                print(f"Warning: Could not load all cartopy features: {e}")
                # Continue without some features
                pass
        except Exception as e:
            print(f"Error with cartopy, falling back to basic map: {e}")
            HAS_CARTOPY = False
    
    if not HAS_CARTOPY:
        # Fallback: Basic matplotlib map
        print("Using basic matplotlib map...")
        fig, ax = plt.subplots(figsize=(14, 10))
        ax.set_xlim(5, 15)
        ax.set_ylim(47, 56)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3, linestyle='--')
        ax.set_xlabel('Longitude / Längengrad / 经度', fontsize=10)
        ax.set_ylabel('Latitude / Breitengrad / 纬度', fontsize=10)
    
    # Coordinates (Hamburg, Germany)
    hamburg_lat, hamburg_lon = 53.5511, 9.9937
    
    # Major distribution centers and markets
    locations = {
        'Hamburg (Production)': {
            'coords': (hamburg_lon, hamburg_lat),
            'type': 'production',
            'color': 'red',
            'size': 300
        },
        'Berlin': {
            'coords': (13.4050, 52.5200),
            'type': 'distribution',
            'color': 'blue',
            'size': 150
        },
        'Munich': {
            'coords': (11.5820, 48.1351),
            'type': 'distribution',
            'color': 'blue',
            'size': 150
        },
        'Cologne': {
            'coords': (6.9603, 50.9375),
            'type': 'distribution',
            'color': 'blue',
            'size': 150
        },
        'Amsterdam': {
            'coords': (4.9041, 52.3676),
            'type': 'market',
            'color': 'green',
            'size': 100
        },
        'Vienna': {
            'coords': (16.3738, 48.2082),
            'type': 'market',
            'color': 'green',
            'size': 100
        },
        'Zurich': {
            'coords': (8.5417, 47.3769),
            'type': 'market',
            'color': 'green',
            'size': 100
        }
    }
    
    # Plot locations
    for name, info in locations.items():
        lon, lat = info['coords']
        color = info['color']
        size = info['size']
        
        if HAS_CARTOPY:
            ax.scatter(lon, lat, c=color, s=size, alpha=0.7, 
                      transform=ccrs.PlateCarree(), 
                      edgecolors='black', linewidths=1.5, zorder=5)
            # Add labels
            ax.text(lon + 0.2, lat + 0.1, name, 
                   transform=ccrs.PlateCarree(), 
                   fontsize=8, ha='left', va='bottom',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7))
        else:
            ax.scatter(lon, lat, c=color, s=size, alpha=0.7, 
                      edgecolors='black', linewidths=1.5, zorder=5)
            ax.text(lon + 0.2, lat + 0.1, name, 
                   fontsize=8, ha='left', va='bottom',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7))
    
    # Draw supply chain routes
    routes = [
        (hamburg_lon, hamburg_lat, 13.4050, 52.5200, 'Berlin'),
        (hamburg_lon, hamburg_lat, 11.5820, 48.1351, 'Munich'),
        (hamburg_lon, hamburg_lat, 6.9603, 50.9375, 'Cologne'),
        (6.9603, 50.9375, 4.9041, 52.3676, 'Amsterdam'),
        (11.5820, 48.1351, 16.3738, 48.2082, 'Vienna'),
        (11.5820, 48.1351, 8.5417, 47.3769, 'Zurich'),
    ]
    
    for route in routes:
        x1, y1, x2, y2, name = route
        if HAS_CARTOPY:
            ax.plot([x1, x2], [y1, y2], 'b--', linewidth=1.5, alpha=0.5,
                   transform=ccrs.PlateCarree(), zorder=3)
        else:
            ax.plot([x1, x2], [y1, y2], 'b--', linewidth=1.5, alpha=0.5, zorder=3)
    
    # Create legend
    legend_elements = [
        plt.scatter([], [], c='red', s=300, edgecolors='black', linewidths=1.5, 
                   label='Production / Produktion / 生产'),
        plt.scatter([], [], c='blue', s=150, edgecolors='black', linewidths=1.5,
                   label='Distribution Center / Vertriebszentrum / 分销中心'),
        plt.scatter([], [], c='green', s=100, edgecolors='black', linewidths=1.5,
                   label='Market / Markt / 市场'),
        plt.Line2D([0], [0], color='blue', linestyle='--', linewidth=1.5,
                  label='Supply Route / Lieferroute / 供应路线')
    ]
    
    ax.legend(handles=legend_elements, loc='upper left', fontsize=9,
             title='Legend / Legende / 图例', title_fontsize=10,
             framealpha=0.9)
    
    # Title (trilingual)
    title = ('Fritz-Kola Supply Chain Map / '
             'Fritz-Kola Supply-Chain-Karte / '
             'Fritz-Kola 供应链地图')
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    
    # Save figure
    output_file = 'fritz-kola-supply-chain-map.png'
    print(f"Saving map to {output_file}...")
    try:
        plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"✓ Map saved successfully to {output_file}")
        plt.close(fig)  # Close figure to free memory
    except Exception as e:
        print(f"Error saving map: {e}")
        raise
    
    return output_file

def create_manufacturer_location_map():
    """Create a detailed map showing manufacturer location in Hamburg"""
    
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Hamburg area coordinates
    hamburg_center_lat, hamburg_center_lon = 53.5511, 9.9937
    
    # Set map extent (Hamburg region) - adjusted to prevent overlap
    lat_range = 0.25
    lon_range = 0.35
    ax.set_xlim(hamburg_center_lon - lon_range, hamburg_center_lon + lon_range)
    ax.set_ylim(hamburg_center_lat - lat_range, hamburg_center_lat + lat_range)
    ax.set_aspect('equal')
    
    # Draw Hamburg outline (simplified)
    hamburg_box = mpatches.Rectangle(
        (hamburg_center_lon - 0.2, hamburg_center_lat - 0.15),
        0.4, 0.3,
        linewidth=2, edgecolor='navy', facecolor='lightblue', alpha=0.3
    )
    ax.add_patch(hamburg_box)
    
    # Key locations in Hamburg - adjusted to prevent overlap
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
    
    # Add grid
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlabel('Longitude / Längengrad / 经度', fontsize=11)
    ax.set_ylabel('Latitude / Breitengrad / 纬度', fontsize=11)
    
    # Legend
    legend_elements = [
        plt.scatter([], [], c='red', s=400, marker='o', edgecolors='black', linewidths=2,
                   label='Production Facility / Produktionsstätte / 生产设施'),
        plt.scatter([], [], c='blue', s=200, marker='s', edgecolors='black', linewidths=2,
                   label='Port / Hafen / 港口'),
        plt.scatter([], [], c='green', s=150, marker='^', edgecolors='black', linewidths=2,
                   label='City Center / Stadtzentrum / 市中心')
    ]
    
    ax.legend(handles=legend_elements, loc='upper right', fontsize=9,
             title='Legend / Legende / 图例', title_fontsize=10,
             framealpha=0.9)
    
    # Title
    title = ('Fritz-Kola Manufacturer Location / '
             'Fritz-Kola Herstellerstandort / '
             'Fritz-Kola 制造商位置')
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    
    # Save figure
    output_file = 'fritz-kola-manufacturer-map.png'
    print(f"Saving manufacturer map to {output_file}...")
    try:
        plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"✓ Manufacturer map saved successfully to {output_file}")
        plt.close(fig)  # Close figure to free memory
    except Exception as e:
        print(f"Error saving manufacturer map: {e}")
        raise
    
    return output_file

if __name__ == '__main__':
    try:
        print("=" * 60)
        print("Fritz-Kola Map Generator")
        print("=" * 60)
        
        print("\n[1/2] Generating supply chain map...")
        create_supply_chain_map()
        
        print("\n[2/2] Generating manufacturer location map...")
        create_manufacturer_location_map()
        
        print("\n" + "=" * 60)
        print("✓ SUCCESS! Maps generated successfully.")
        print("=" * 60)
        print("\nGenerated files:")
        print("  - fritz-kola-supply-chain-map.png")
        print("  - fritz-kola-manufacturer-map.png")
        print("\nYou can now include these images in your LaTeX document.")
        
    except Exception as e:
        print("\n" + "=" * 60)
        print("✗ ERROR: Map generation failed!")
        print("=" * 60)
        print(f"Error details: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
