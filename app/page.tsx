import Hero from '@/components/Hero';
import Projects from '@/components/Projects';
import Footer from '@/components/Footer';

export default function Home() {
  return (
    <main className="max-w-5xl mx-auto px-4">
      <Hero />
      <Projects />
      <Footer />
    </main>
  );
}