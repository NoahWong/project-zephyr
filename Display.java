import ij.ImagePlus;
import ij.ImageStack;
import ij.io.FileSaver;
import ij.process.ByteProcessor;

import java.util.*;
import java.awt.Color;
import java.awt.Image;
import java.awt.image.BufferedImage;

public class Display 
{
	private int width;
	private int height;
	private final static int TYPE = BufferedImage.TYPE_INT_ARGB;
	private ImagePlus img;
	private FileSaver saver;
	private final static String path = "C:\\Users\\Noah\\Desktop\\Zephyrgram.png";
	public Display(int width, int height)
	{
		this.width = width;
		this.height = height;
		img = new ImagePlus("Name", new BufferedImage(width, height, TYPE));
		saver = new FileSaver(img);
		
	}
	public void setPixel(int x, int y, Color c)
	{
		img.getBufferedImage().setRGB(x, y, c.getRGB());
	}
	public void setPixels(Color[][] matrix)
	{
		if(matrix.length > width || matrix[0].length > height)
		{
			throw new IllegalArgumentException();
		}
		else
		{
			for(int x = 0; x < matrix.length; x++)
			{
				for(int y = 0; y < matrix[x].length; y++)
				{
					setPixel(x, y, matrix[x][y]);
				}
			}
		}
	}
	public int polutionToColor(int CO, int H2S)
	{
		Color temp = new Color(CO, H2S, 0);
		return temp.getRGB();
	}
	public void exportImg()
	{
		saver = new FileSaver(img);
		saver.saveAsPng(path);
	}
}
