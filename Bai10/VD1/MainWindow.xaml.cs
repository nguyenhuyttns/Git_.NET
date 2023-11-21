using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace VD1
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void MenuItem211_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("Ban chon menu 211");
        }

        private void MenuItem212_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("Ban chon menu 212");
        }

        private void Menu3_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("Ban chon menu 3");
        }
    }
}
